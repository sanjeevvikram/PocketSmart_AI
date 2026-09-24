const $ = s => document.querySelector(s);
const $$ = s => document.querySelectorAll(s);

function safeNumber(value, fallback = 0) {
    const n = Number(value);
    return Number.isFinite(n) ? n : fallback;
}

function formatINR(value) {
    return `₹${safeNumber(value).toLocaleString('en-IN')}`;
}

function safeText(value, fallback = '') {
    return value === undefined || value === null ? fallback : String(value);
}

$$('.tab').forEach(t => {
    t.onclick = () => {
        $$('.tab').forEach(x => x.classList.remove('active'));

        const activePanel = $('.panel.active');
        if (activePanel) {
            activePanel.classList.remove('active');
        }

        t.classList.add('active');

        const panel = $('#' + t.dataset.tab);
        if (panel) {
            panel.classList.add('active');
        }

        if (t.dataset.tab === 'history') {
            loadHistory();
        }
    };
});

$('#logout').onclick = async () => {
    await api('/api/auth/logout', { method: 'POST' });
    location.href = '/login';
};


function showResult(r) {
    const out = $('#results');

    const planner = safeText(r.planner, 'Planner');
    const summary = safeText(r.summary, 'Plan generated successfully.');
    const sourceNote = safeText(
        r.source_note,
        'Prices and availability should be verified before purchase.'
    );

    const estimatedTotal = safeNumber(r.estimated_total);
    const budget = safeNumber(r.budget);
    const budgetRemaining = safeNumber(
        r.budget_remaining,
        Math.max(budget - estimatedTotal, 0)
    );

    const recommendations = Array.isArray(r.recommendations)
        ? r.recommendations
        : [];

    const allocation =
        r.allocation && typeof r.allocation === 'object'
            ? r.allocation
            : {};


    /* -------------------------
       Budget Allocation
    ------------------------- */

    const allocationEntries = Object.entries(allocation);

    const allocationHtml = allocationEntries.length
        ? `
            <div class="card" style="margin-top:16px;">
                <div class="result-head">
                    <div>
                        <span class="eyebrow">Budget Allocation</span>
                        <h3>Planned spending</h3>
                    </div>
                </div>

                <div>
                    ${allocationEntries.map(([category, amount]) => `
                        <div class="recommendation">
                            <div>
                                <strong>
                                    ${escapeHtml(
                                        category
                                            .replace(/_/g, ' ')
                                            .replace(/\b\w/g, c => c.toUpperCase())
                                    )}
                                </strong>
                            </div>

                            <div class="price">
                                ${formatINR(amount)}
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `
        : `
            <div class="card" style="margin-top:16px;">
                <span class="eyebrow">Budget Allocation</span>
                <p class="muted">
                    Allocation details are not available for this response.
                </p>
            </div>
        `;


    /* -------------------------
       Recommendations
    ------------------------- */

    const recommendationsHtml = recommendations.length
        ? recommendations.map(x => {

            const title = safeText(x.title, 'Recommended item');
            const platform = safeText(x.platform, 'Search');
            const category = safeText(x.category, 'General');
            const reason = safeText(
                x.reason,
                'Recommended based on the selected budget and requirements.'
            );

            const quantity = safeNumber(x.quantity, 1);

            const hasPrice =
                x.estimated_price !== undefined &&
                x.estimated_price !== null &&
                Number.isFinite(Number(x.estimated_price));

            const priceHtml = hasPrice
                ? formatINR(x.estimated_price)
                : 'Price unavailable';

            const url = safeText(x.url, '#');

            return `
                <div class="recommendation">

                    <div>
                        <strong>${escapeHtml(title)}</strong>

                        <div class="muted">
                            ${escapeHtml(platform)}
                            ·
                            ${escapeHtml(category)}
                            ·
                            Qty ${quantity}
                        </div>

                        <div>
                            ${escapeHtml(reason)}
                        </div>

                        ${
                            url !== '#'
                                ? `<a href="${escapeHtml(url)}"
                                      target="_blank"
                                      rel="noopener">
                                      Open search
                                   </a>`
                                : ''
                        }
                    </div>

                    <div class="price">
                        ${priceHtml}
                    </div>

                </div>
            `;
        }).join('')
        : `
            <div class="card">
                <span class="eyebrow">Recommendations</span>
                <p class="muted">
                    No individual recommendations were returned.
                </p>
            </div>
        `;


    /* -------------------------
       Final Result
    ------------------------- */

    out.innerHTML = `
        <div class="card">

            <div class="result-head">

                <div>
                    <span class="eyebrow">
                        ${escapeHtml(planner)}
                    </span>

                    <h2>
                        ${escapeHtml(summary)}
                    </h2>
                </div>

                <div>
                    <strong>
                        ${formatINR(estimatedTotal)}
                    </strong>

                    <div class="muted">
                        ${formatINR(budgetRemaining)}
                        remaining
                    </div>
                </div>

            </div>


            <p class="muted">
                ${r.ai_generated ? 'Gemini generated' : 'Fallback'}
                ·
                ${escapeHtml(sourceNote)}
            </p>


            ${
                budget > 0
                    ? `
                        <div class="card" style="margin-top:16px;">
                            <span class="eyebrow">Total Budget</span>

                            <h3>
                                ${formatINR(budget)}
                            </h3>

                            <div class="muted">
                                Estimated spending:
                                ${formatINR(estimatedTotal)}
                            </div>

                            <div class="muted">
                                Remaining:
                                ${formatINR(budgetRemaining)}
                            </div>
                        </div>
                    `
                    : ''
            }

        </div>

        ${allocationHtml}

        <div class="card" style="margin-top:16px;">

            <div class="result-head">
                <div>
                    <span class="eyebrow">
                        Recommendations
                    </span>

                    <h3>
                        Suggested options
                    </h3>
                </div>
            </div>

            ${recommendationsHtml}

        </div>
    `;

    out.scrollIntoView({
        behavior: 'smooth'
    });
}


$('#homeForm').onsubmit = async e => {
    e.preventDefault();

    const f = new FormData(e.target);

    const items = f.get('items')
        .split('\n')
        .map(x => {
            const [name, q] = x.split(',');

            return {
                name: name.trim(),
                quantity: safeNumber(q || 1, 1)
            };
        })
        .filter(x => x.name);

    const body = {
        budget: safeNumber(f.get('budget')),
        style: f.get('style'),
        rooms: f.get('rooms')
            .split(',')
            .map(x => x.trim())
            .filter(Boolean),
        items,
        notes: f.get('notes')
    };

    try {
        showResult(
            await api('/api/generate-home', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(body)
            })
        );
    } catch (e) {
        alert(e.message);
    }
};


$('#partyForm').onsubmit = async e => {
    e.preventDefault();

    const f = new FormData(e.target);

    const body = {
        budget: safeNumber(f.get('budget')),
        guests: safeNumber(f.get('guests')),
        event_type: f.get('event_type'),
        venue: f.get('venue'),
        date: f.get('date'),
        preferences: f.get('preferences')
    };

    try {
        showResult(
            await api('/api/generate-party', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(body)
            })
        );
    } catch (e) {
        alert(e.message);
    }
};


$('#jewelryForm').onsubmit = async e => {
    e.preventDefault();

    try {
        showResult(
            await api('/api/generate-jewelry', {
                method: 'POST',
                body: new FormData(e.target)
            })
        );
    } catch (e) {
        alert(e.message);
    }
};


async function loadHistory() {
    try {
        const rows = await api('/api/history');

        $('#historyList').innerHTML = rows.length
            ? rows.map(x => `
                <div class="card">

                    <strong>
                        ${escapeHtml(x.planner)}
                    </strong>

                    <div class="muted">
                        ${new Date(x.created_at).toLocaleString()}
                    </div>

                    <pre>
                        ${escapeHtml(
                            JSON.stringify(x.request, null, 2)
                        )}
                    </pre>

                </div>
            `).join('')
            : '<p class="muted">No recommendations yet.</p>';

    } catch (e) {
        $('#historyList').innerHTML = `
            <p class="error">
                ${escapeHtml(e.message)}
            </p>
        `;
    }
}


api('/api/auth/session-info')
    .catch(() => location.href = '/login');
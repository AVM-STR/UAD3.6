"""
UAD 2.6 → 3.6 Transition Resource
Presented by Absolute Value Management & A-Tech Appraisal Co.
"""

import os
import base64
import json
import streamlit as st

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

try:
    from reportlab.lib.pagesizes import letter
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False

ATECH_LOGO = os.path.join(os.path.dirname(__file__), "atech_logo.png")
AVM_LOGO   = os.path.join(os.path.dirname(__file__), "avm_logo.png")

st.set_page_config(
    page_title="UAD 3.6 Transition Guide",
    page_icon="🏠",
    layout="wide"
)

# ── Sidebar Navigation ─────────────────────────────────────────────────────────
with st.sidebar:
    if os.path.exists(AVM_LOGO):
        st.image(AVM_LOGO, width=160)
    if os.path.exists(ATECH_LOGO):
        st.image(ATECH_LOGO, width=160)
    st.title("UAD 3.6 Transition Guide")
    st.divider()
    selection = st.selectbox(
        "Select a Section",
        [
            "📄 Assignment Intake",
            "🤝 Working With Your AMC",
            "📊 What Changed",
            "🚀 Before Your First 3.6 Order",
            "🔍 Inspection Guide",
            "✅ Inspection Checklist",
            "🌍 Site Influence Guide",
            "📐 Sketch & ANSI",
            "🏠 C & Q Ratings",
            "🗺️ Field Mapper",
            "❓ FAQ / Revision Responses",
            "💻 Software & Tools",
            "📚 Training Resources",
        ],
        label_visibility="collapsed"
    )
    st.divider()
    st.info("⏱️ **Nov 2, 2026** — UAD 3.6 mandatory")
    st.caption("Presented by Absolute Value Management & A-Tech Appraisal Co.")

# ── Main Header ────────────────────────────────────────────────────────────────
st.title(selection)

# ── Timeline banner (always visible) ──────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.info("**Sept 8, 2025**\nLimited Production begins")
with c2:
    st.success("**Jan 26, 2026**\nBroad Production — both accepted ✅")
with c3:
    st.warning("**Nov 2, 2026**\n3.6 MANDATORY — 2.6 rejected")
with c4:
    st.error("**May 3, 2027**\n2.6 pipeline fully retired")

st.divider()

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — WHAT CHANGED
# ══════════════════════════════════════════════════════════════════════════════
if selection == "📊 What Changed":
    st.subheader("What's the same, what changed, what's new, and what's gone")
    st.markdown("The most important thing to understand first: **UAD 3.6 does not change how you estimate value.** It changes how that work is reported and what data is collected. USPAP obligations are unchanged. Your professional judgment is still the foundation of every report.")

    col_l, col_r = st.columns(2)
    with col_l:
        st.success("🟢 **Same** — no change")
        st.warning("🟡 **Changed** — same analysis, different reporting")
    with col_r:
        st.info("🔵 **New** — didn't exist in 2.6")
        st.error("🔴 **Gone** — retired in 3.6")

    st.divider()

    sections = {
        "📄 Forms & Report Structure": [
            ("🟡", "Form selection", "One dynamic URAR replaces all legacy forms — 1004, 1073, 2055, 2055-EXT, 1004D, and all hybrid/exterior variants. Sections turn on and off based on property type and assignment. No more form numbers."),
            ("🔴", "1004MC Market Conditions form", "Eliminated entirely. Market conditions analysis is now embedded in the URAR Market section as structured fields. Time adjustments still required and must be supported — but not via the MC grid."),
            ("🟡", "Scope of work", "Same analytical obligation. More structured fields, less free-text narrative."),
            ("🟢", "USPAP compliance", "Unchanged. UAD 3.6 is a reporting format change, not a USPAP change."),
            ("🟢", "How value is estimated", "Exactly the same. Sales comparison, cost, income approaches — all unchanged."),
        ],
        "🏠 Condition & Quality Ratings": [
            ("🟡", "C1–C6 Condition rating", "Now three separate ratings: Exterior Condition + Interior Condition → reconciled to Overall. Previously one rating for the whole property."),
            ("🟡", "Q1–Q6 Quality rating", "Same structure change — Exterior Quality + Interior Quality → reconciled to Overall. Quality is still absolute, not relative to local market."),
            ("🟢", "C6 rule", "If any component is C6, overall must be C6. Unchanged. Fannie allows C5 as-is in some cases; Freddie requires C4 minimum for delivery."),
            ("🟡", "Defects documentation", "C5 or C6 now requires itemized structured list: location, description, impact on soundness, recommended action, estimated repair cost. Previously narrative only."),
            ("🔵", "As-Is + Subject-to-Repair ratings", "When repairs required: must report BOTH As-Is Overall Condition AND Condition Subject to Repair as two explicit separate ratings."),
        ],
        "🍳 Kitchen & Bathroom Reporting": [
            ("🔴", "'Not updated / Updated / Remodeled' checkbox", "Retired entirely. Replaced by structured Kitchen and Bathroom Details sections."),
            ("🟡", "Kitchen reporting", "Per-kitchen structured section: update status + approximate year + condition rating (C1–C6) + brief description. Every kitchen reported individually."),
            ("🟡", "Bathroom reporting", "Per-bathroom structured section: same structure as kitchen. Every bathroom including half baths reported individually."),
        ],
        "🌍 Site & Location": [
            ("🟡", "View / location influence", "Replaced by Site Influence section. Now captures: onsite / bordering / distant AND positive / neutral / negative. A pond on the lot vs a water view from a distance are now distinct reportable data points."),
            ("🟡", "Zoning, utilities, site features", "Significantly expanded structured fields. The Site section is 30 pages in the URAR Reference Guide — second largest chapter after the Sales Comparison Approach (67 pages)."),
        ],
        "📊 Sales Comparison Approach": [
            ("🟢", "Comparable selection and analysis", "Same process, same professional judgment. More structured fields, less free-text narrative."),
            ("🟡", "Time adjustments", "1004MC is gone. Time adjustments still required when market warrants. The decision NOT to adjust requires the same rigor as the decision to adjust."),
            ("🟢", "Actual age in comp grid", "Only actual age in the grid. Effective age moves to narrative commentary."),
            ("🟡", "GLA measurement", "ANSI Z765-2021 formalized. Above-grade finished area must be broken out by floor. UCDP compliance rules will enforce ANSI logic on submission."),
            ("🔴", "Street inspection of comparable sales", "No longer required. Front photo of comp still required but the physical drive-by has been retired. Photo can be sourced from MLS or other reliable source."),
        ],
        "🏗️ Special Features": [
            ("🔵", "ADU section", "New dedicated section. Effective Mar 21, 2026: expanded ADU eligibility ONLY available with UAD 3.6 submissions. ADU rental income can count toward qualifying income under certain conditions."),
            ("🟡", "Manufactured housing terminology", "Effective Mar 31, 2026: 'single-width' and 'multi-width' replace 'single-section' and 'multi-section' in all UAD 3.6 reports."),
            ("🔵", "Broadband internet availability", "New required field — must report whether broadband is available at the property. GSE has a specific definition — see Appendix F-1."),
            ("🔵", "Disaster mitigation features", "New section — storm shutters, hurricane straps, flood vents, seismic retrofitting. If the section is included, commentary is required."),
            ("🔵", "Access road type", "New structured field — type of road providing access (public paved, private, gravel, dirt, etc.)."),
        ],
    }

    for section, items in sections.items():
        st.markdown(f"### {section}")
        for status, title, detail in items:
            with st.expander(f"{status} {title}"):
                st.write(detail)
        st.write("")

    st.caption("Sources: Fannie Mae & Freddie Mac UAD Inspection and Reporting Tips (Oct 2025), UAD 3.6 FAQ, McKissock Learning, Working RE, Appraiser eLearning.")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — FIELD MAPPER
# ══════════════════════════════════════════════════════════════════════════════
elif selection == "🗺️ Field Mapper":
    st.subheader("Field Mapper — find where your 2.6 data lives in 3.6")
    st.caption("Type any field name, section, or keyword from your current 1004 to find its UAD 3.6 equivalent.")

    search = st.text_input("🔍 Search fields", placeholder="e.g. View, GLA, condition, kitchen, market conditions...")

    field_map = [
        ("View", "Site Influence", "Changed", "Now captures proximity (onsite / bordering / distant) AND direction of influence (positive / neutral / negative). Much more granular than the old View field."),
        ("Location", "Site Influence", "Changed", "Merged with View into the expanded Site Influence section. Neighborhood, proximity to amenities, and external influences all captured here."),
        ("Condition (overall)", "Overall Condition Rating", "Changed", "Still C1–C6 but now derived from separate Exterior and Interior condition ratings. Cannot assign overall without first rating each component separately."),
        ("Quality (overall)", "Overall Quality Rating", "Changed", "Still Q1–Q6 but now derived from separate Exterior and Interior quality ratings."),
        ("GLA / Gross Living Area", "Above-Grade Finished Area (by floor)", "Changed", "Must now be broken out by floor — first floor, second floor, etc. ANSI Z765-2021 enforced. NSFA (Nonstandard Finished Area) reported in a separate dedicated field."),
        ("Basement finished area", "Below-Grade Finished Area", "Same", "Same concept — dedicated structured field. Still not included in above-grade GLA."),
        ("Kitchen: Updated / Not Updated / Remodeled", "Kitchen Details Section", "Changed", "Per-kitchen section: update status + approximate year of update + condition rating (C1–C6) + brief description. Old checkbox is retired."),
        ("Bathroom: Updated / Not Updated / Remodeled", "Bathroom Details Section", "Changed", "Per-bathroom section: same structure. Every bathroom including half baths reported individually. Old checkbox is retired."),
        ("1004MC / Market Conditions", "Market Section (embedded in URAR)", "Gone → Changed", "1004MC is retired. Market conditions analysis is now built into the URAR Market section with structured fields. Time adjustments still required."),
        ("Actual Age", "Actual Age", "Same", "Still reported in the comp grid. Only actual age required — effective age moves to narrative commentary."),
        ("Effective Age", "Narrative commentary", "Changed", "No longer a required grid field. Discuss in narrative when relevant."),
        ("Site: Zoning", "Zoning (structured)", "Changed", "More structured fields. Zoning compliance, legal nonconforming, and zoning description all captured separately."),
        ("Site: Utilities", "Utilities (structured)", "Changed", "Expanded — now captures utility type, whether public or private, and whether connected to each utility individually."),
        ("Outbuildings", "Additional Structures section", "Changed", "New dedicated section. Must document utilities extended to each outbuilding."),
        ("ADU / Accessory Unit", "ADU Section", "New", "New dedicated section — GLA, bed/bath, kitchen, separate entrance, condition, legal status. Required when ADU is present."),
        ("Highest and Best Use", "Highest and Best Use", "Same", "Same analysis and conclusion required. Reporting format more structured."),
        ("Cost Approach", "Cost Approach section", "Same", "Same — included when section is triggered by property type or assignment."),
        ("Income Approach", "Income Approach section", "Changed", "Same analytical requirement. More structured data fields for rental income, GRM, and capitalization rate."),
        ("Comparable photos", "Comparable photos", "Same", "Front photo of each comp still required. Drive-by street inspection no longer required."),
        ("Subject photos", "Subject photos", "Same", "Front, rear, and street scene still required. Additional photos required when project deficiency observed (condos)."),
        ("Ceiling height", "Ceiling Height (required field)", "New", "New required field — always. Report Field ID 10.045. Tied to ANSI 7-foot rule."),
        ("Broadband / internet", "Broadband Availability", "New", "New required field — must report whether broadband internet is available at the property."),
        ("Access road", "Access Road Type", "New", "New structured field — type of road providing access to property."),
        ("Manufactured home: single-section", "Single-width", "Changed", "Effective Mar 31, 2026: 'single-width' replaces 'single-section'."),
        ("Manufactured home: multi-section", "Multi-width", "Changed", "Effective Mar 31, 2026: 'multi-width' replaces 'multi-section'."),
        ("Disaster mitigation", "Disaster Mitigation Features section", "New", "New section — storm shutters, hurricane straps, flood vents, seismic features. Commentary required if section included."),
        ("Form 1004", "Dynamic URAR", "Gone", "Retired Nov 2, 2026. All 1–4 unit properties use the single dynamic URAR."),
        ("Form 1073 (condo)", "Dynamic URAR (condo sections)", "Gone", "Retired. URAR activates condo-specific sections automatically."),
        ("Form 2055 (exterior only)", "Dynamic URAR (exterior assignment)", "Gone", "Retired. URAR adapts to exterior-only assignment type."),
        ("Form 1004D (update/completion)", "Restricted Appraisal Update Report / Completion Report", "Changed", "Separate dedicated reports — not a form number. Must be submitted to UCDP."),
    ]

    if search:
        q = search.lower()
        filtered = [f for f in field_map if
                    q in f[0].lower() or q in f[1].lower() or
                    q in f[2].lower() or q in f[3].lower()]
    else:
        filtered = field_map

    st.write(f"**{len(filtered)} field{'s' if len(filtered) != 1 else ''}**")
    st.divider()

    status_icons = {"Same": "🟢", "Changed": "🟡", "New": "🔵",
                    "Gone": "🔴", "Gone → Changed": "🔴"}

    for uad26, uad36, status, notes in filtered:
        icon = status_icons.get(status, "⚪")
        with st.expander(f"{icon} **{uad26}** → {uad36}  `{status}`"):
            st.write(notes)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — INSPECTION GUIDE
# ══════════════════════════════════════════════════════════════════════════════
elif selection == "🔍 Inspection Guide":
    st.subheader("What to collect at every inspection under UAD 3.6")
    st.warning("UAD 3.6 requires significantly more structured data collected in the field. Plan your inspections accordingly — some of this requires new tools or conversations with the owner/agent that weren't part of your workflow before.")

    st.markdown("### 🔧 What to bring")
    tools = [
        ("Laser distance measurer", "Required for ceiling height — a mandatory field at every inspection. A tape measure and ladder is not practical or safe. Invest in a quality laser measurer if you haven't already."),
        ("Mobile device with UAD 3.6 software", "The volume of new structured data fields makes mobile entry at the inspection far more efficient than clipboard + office entry. This is the workflow UAD 3.6 is designed around."),
        ("FCC broadband map reference", "You'll need to confirm broadband availability at the subject. Pull the address in the FCC broadband map (broadbandmap.fcc.gov) before or during inspection."),
    ]
    for tool, note in tools:
        with st.expander(f"🔧 {tool}"):
            st.write(note)

    st.divider()
    st.markdown("### 🔵 New — must now measure or collect")

    new_items = [
        ("Ceiling height — every room / level", "Required field (Report Field ID 10.045) — always. Tied to ANSI 7-foot rule: if more than half a room's area is under 7 ft, that portion cannot be included in GLA. Use a laser measurer."),
        ("Walls and ceiling materials / type", "Required structured field in the Interior Features table — select from defined enumerations. Always displays, always required."),
        ("Nonstandard Finished Area (NSFA)", "Any finished space that doesn't meet ANSI must be measured and reported separately from GLA. Must explain why — e.g. 'sloping ceiling under 7 ft'. Common in finished attics, bonus rooms with knee walls."),
        ("Kitchen details — per kitchen", "For every kitchen: update status, approximate year of update, condition rating (C1–C6), brief description. Collect at inspection — don't try to fill this in from MLS photos."),
        ("Bathroom details — per bathroom", "For every bathroom including half baths: same fields as kitchen. Count and document every bathroom individually."),
        ("Exterior quality — separate observation", "Assess exterior components separately: siding, roof, foundation, windows, trim, architectural detail. Note these distinctly from interior quality."),
        ("Exterior condition — separate observation", "Assess exterior condition separately from interior. Note specific deficiencies with location and description for any C5 or C6 items."),
        ("Interior quality — separate observation", "Assess interior components separately: flooring, trim, cabinetry, fixtures, countertops, built-ins. Note level of finish throughout."),
        ("Interior condition — separate observation", "Assess interior condition separately. If C5 or C6: document location, description, impact on soundness, recommended action, and estimated repair cost for each deficiency."),
        ("Roof replacement estimate", "New structured field — when was the roof last replaced? Ask the owner or agent. Can also check permit records if available."),
        ("Outbuilding utilities", "If outbuildings present: which utilities have been extended to each (electric, water, HVAC, etc.). Document each outbuilding separately."),
        ("Broadband internet availability", "New required field. Verify via FCC broadband map or ask the owner. The GSE has a specific definition of broadband — check Appendix F-1 for the allowable enumerations."),
        ("Access road type", "New structured field — type of road providing access to the property (public paved, private paved, gravel, dirt, etc.)."),
        ("Site influence — proximity and direction", "New structure: Is the influence onsite / bordering / distant? Is it positive / neutral / negative? More precise than the old View field."),
        ("ADU — if present", "Dedicated section: unit type, GLA, bed/bath count, kitchen presence, separate entrance, condition, and whether legally permitted. Collect all details at inspection."),
        ("Disaster mitigation features", "If present: storm shutters, hurricane straps, flood vents, seismic retrofitting, impact glass. Note presence and type at inspection."),
    ]
    for title, detail in new_items:
        with st.expander(f"🔵 {title}"):
            st.write(detail)

    st.divider()
    st.markdown("### 🟡 Changed — same observation, captured differently")
    changed_items = [
        ("Above-grade GLA — per floor breakdown", "Previously reported as one total. Now must break out by floor — first floor, second floor, etc. UCDP will validate that floors sum correctly."),
        ("NSFA — separate from GLA", "Finished space that doesn't meet ANSI now goes in a dedicated NSFA field, not lumped into GLA or addenda."),
    ]
    for title, detail in changed_items:
        with st.expander(f"🟡 {title}"):
            st.write(detail)

    st.divider()
    st.markdown("### 🔴 Gone — no longer required at inspection")
    gone_items = [
        ("Street inspection of comparable sales", "No longer required. Front photo of each comp still required but the physical drive-by inspection from the street has been retired. Photo can be sourced from MLS or other reliable data source."),
    ]
    for title, detail in gone_items:
        with st.expander(f"🔴 {title}"):
            st.write(detail)

    st.caption("Source: GSE Inspection and Reporting Tips (Oct 2025), Appendix F-1 URAR Reference Guide, ANSI Z765-2021.")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 4 — C & Q RATINGS
# ══════════════════════════════════════════════════════════════════════════════
elif selection == "🏠 C & Q Ratings":
    st.subheader("Condition & Quality Ratings")

    rating_tab1, rating_tab2, rating_tab3 = st.tabs([
        "🏠 Condition (C1–C6)",
        "🔨 Quality (Q1–Q6)",
        "⚖️ How to Reconcile"
    ])

    with rating_tab1:
        st.info("**Key change:** Condition is now reported separately for Exterior and Interior, then reconciled to an Overall rating. If ANY component is C6, the overall must be C6. Fannie Mae allows C5 as-is in some cases; Freddie Mac requires C4 minimum for loan delivery.")

        conditions = [
            ("C1", "New / Like New",
             "New or nearly new. No physical wear on any component. All major and minor elements are in like-new condition. Rebuilt homes may qualify if on a completely new foundation with fully remanufactured materials.",
             "Use for new construction and very recent gut rehabs to the studs. Rarely seen on resale. If you're questioning whether it's C1, it probably isn't.",
             "✅ Fannie: eligible as-is | ✅ Freddie: eligible as-is"),
            ("C2", "Extensive Renovation",
             "Extensively renovated to resemble new construction. Most components recently replaced or refinished. Minimal physical depreciation, no deferred maintenance, nothing requires repair.",
             "The per-kitchen and per-bathroom detail in 3.6 makes this harder to assign loosely. Every major system should be new or like-new. Your kitchen and bathroom details must support this rating.",
             "✅ Fannie: eligible as-is | ✅ Freddie: eligible as-is"),
            ("C3", "Well Maintained / Updated",
             "Well maintained with limited physical depreciation. Some components may show minor wear but all functional systems are working properly. Some updating may be present.",
             "Most move-in ready properties with recent updates but not full renovation. Very common in well-maintained New England stock. The most common rating in the upper-middle price range.",
             "✅ Fannie: eligible as-is | ✅ Freddie: eligible as-is"),
            ("C4", "Average / Adequate",
             "Adequately maintained with some physical depreciation. Normal wear and tear. All functional systems working. No immediate repairs required but may have deferred maintenance items.",
             "The baseline for typical resale. Dated but functional kitchens/baths, normal aging. Very common in pre-1970 RI/MA housing stock. Colonial-era homes often rate C4 despite their age — condition is about current state, not age.",
             "✅ Fannie: eligible as-is | ✅ Freddie: eligible as-is"),
            ("C5", "Fair / Deferred Maintenance",
             "Obvious deferred maintenance and/or physical deterioration. Some components need repair or replacement. Major systems may be functional but near end of useful life.",
             "Requires itemized defect list in 3.6 — location, description, impact, action, estimated cost. Fannie allows C5 as-is in some cases; Freddie requires repairs to C4 minimum before delivery. Always check lender overlays.",
             "⚠️ Fannie: allowed as-is (lender dependent) | ❌ Freddie: must repair to C4"),
            ("C6", "Significant Damage / Safety Concern",
             "Significant damage, serious deferred maintenance, or conditions affecting safety, soundness, or structural integrity. May be uninhabitable or pose health/safety risks.",
             "If ANY single component is C6, the overall must be C6. Requires full itemized defect list. Must be appraised subject-to repairs. Flag immediately — lender eligibility issues are certain.",
             "❌ Fannie: must be subject-to | ❌ Freddie: must be subject-to"),
        ]

        for code, label, definition, notes, eligibility in conditions:
            with st.expander(f"**{code} — {label}**"):
                st.write(definition)
                st.caption(f"📝 Field notes: {notes}")
                st.caption(f"🏦 Eligibility: {eligibility}")

    with rating_tab2:
        st.info("**Key change:** Quality is now reported separately for Exterior and Interior, then reconciled to an Overall rating. Quality is absolute — a Q3 is a Q3 whether it's in Providence or Newport. Local market norms, price point, and neighborhood do not determine the quality rating.")

        qualities = [
            ("Q1", "Exceptional / Custom",
             "Custom architecture, outstanding workmanship, and premium materials throughout — often imported or specialty items. Extensive ceiling treatments, rare flooring with custom inlay, top-grade cabinetry and countertops throughout. Every component reflects exceptional design.",
             "Very rare. Most markets have no Q1 properties. If you're questioning whether it qualifies, it doesn't. Common misconception: an expensive home is not automatically Q1."),
            ("Q2", "High Quality / Custom",
             "Still custom, but not at the absolute top tier. High-quality materials and consistently strong workmanship. May be custom-built or part of a high-quality development. High-end finishes throughout with some premium or specialty items.",
             "May be the highest rating seen in many markets. Common in higher-end coastal RI and South Shore MA. Distinguishing Q1 from Q2: Q1 has imported/specialty items throughout; Q2 has high quality but not necessarily the absolute best available."),
            ("Q3", "Good Quality / Above Average",
             "Solidly constructed with good materials, though not custom throughout. Often includes upgraded finishes mixed with some standard components. Better than production-grade but not fully custom.",
             "Most common in the upper-middle price range. Upgraded kitchen and baths with builder-grade framing and exterior. A home with granite counters and hardwood floors but vinyl siding and standard windows is typically Q3."),
            ("Q4", "Average / Standard",
             "Standard or builder-grade materials and construction. Meets code requirements. No significant upgrades. Represents the majority of production housing. Functional throughout with standard finishes.",
             "The baseline for most residential construction. Colonial-era New England stock typically falls here despite age — quality is about construction and materials, not condition or age. Don't confuse age with quality."),
            ("Q5", "Fair / Below Average",
             "Below-standard materials or workmanship. May show significant deficiencies in design, construction, or finish. Functional but lacks quality. May include significant DIY construction or non-professional work.",
             "Rare in typical residential lending. More common in older worker housing, self-built structures, or properties with significant inferior improvements. Flag for lender review."),
            ("Q6", "Poor / Substandard",
             "Construction that may not meet basic building standards. Often built without professional oversight or adherence to modern codes. Small rooms, low ceilings, minimal storage, basic fixtures only. May be unsuitable for year-round habitation.",
             "Very rarely assigned. Flag immediately — lender eligibility issues are likely. Distinguish from C6 (condition): Q6 is about construction quality, not current damage or deferred maintenance."),
        ]

        for code, label, definition, notes in qualities:
            with st.expander(f"**{code} — {label}**"):
                st.write(definition)
                st.caption(f"📝 Field notes: {notes}")

    with rating_tab3:
        st.markdown("### How to reconcile Exterior + Interior → Overall")
        st.markdown("""
Under UAD 3.6 you assign ratings in this order:

**Step 1 — Exterior Quality and Condition**
Assess the exterior components independently: siding, roof material and design, foundation, windows and doors, trim, architectural detail. What is the quality of these materials and construction? What is their current condition?

**Step 2 — Interior Quality and Condition**
Assess the interior components independently: flooring, wall and ceiling finishes, trim work, cabinetry, countertops, fixtures, built-ins. Kitchen details and bathroom details feed directly into this assessment.

**Step 3 — Reconcile to Overall**
The overall rating must be consistent with and supported by both the exterior and interior ratings you've already assigned. It cannot be assigned in isolation.

**Key reconciliation rules:**
- A single standout feature (like a high-end kitchen) does not automatically change the overall quality rating — it influences the interior quality assessment which then flows into the overall.
- For condition: if ANY component is C6, the overall must be C6. There is no exception.
- For quality: the overall should reflect the predominant quality level of the property as a whole. A Q4 exterior and Q3 interior might reconcile to Q3 or Q4 depending on the relative weight and significance of each.
- The overall rating must make sense when compared against all the structured data you've entered elsewhere in the report. Automated review tools will check for inconsistencies.

**The new format makes inconsistencies easy to detect.**
If your overall condition rating doesn't align with your kitchen details, bathroom details, and interior condition rating, the reviewer — and the UCDP compliance checker — will flag it. Think of the structured fields as your support for the overall rating, not separate disconnected data points.
        """)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 5 — SKETCH & ANSI
# ══════════════════════════════════════════════════════════════════════════════
elif selection == "📐 Sketch & ANSI":
    st.subheader("Sketch & ANSI Z765-2021 Measurement Guide")
    st.info("ANSI Z765-2021 is now formalized in UAD 3.6 and enforced by UCDP compliance rules. The way above-grade finished area is measured, reported, and broken out by floor has specific requirements that will be checked on submission.")

    st.markdown("### The core ANSI rules")
    ansi_rules = [
        ("7-foot ceiling height rule", "A room or area must have a ceiling height of at least 7 feet over more than half its floor area to qualify as finished living area. If less than half the area meets the 7-foot requirement, the entire area fails and cannot be counted as GLA."),
        ("Above-grade only", "GLA includes only finished areas above grade. Below-grade areas (including fully finished walk-out basements) are reported separately as Below-Grade Finished Area — never in GLA."),
        ("Must be finished", "An area must be finished (with flooring, walls, and ceiling) to be counted. Unfinished attic space, unfinished bonus rooms, and storage areas do not count regardless of ceiling height."),
        ("Heated and cooled", "Above-grade GLA must be directly accessible from the main living area and suitable for year-round use. Spaces accessible only from the exterior or requiring passage through unfinished areas may not qualify."),
        ("Per floor breakdown required", "In UAD 3.6, above-grade GLA must be reported by floor — first floor total, second floor total, etc. UCDP validates that floors sum to the total reported GLA."),
        ("Consistency across comps", "The same measurement methodology must be applied consistently to the subject and all comparable sales. If using ANSI for the subject, you must apply ANSI-consistent measurements to comps or explain the deviation."),
    ]
    for title, detail in ansi_rules:
        with st.expander(f"📐 {title}"):
            st.write(detail)

    st.divider()
    st.markdown("### Common New England scenarios")
    ne_scenarios = [
        ("Finished attic with sloped ceiling", "This is the most common ANSI challenge in New England. Measure the area where ceiling height is 7 feet or more. The area under the slope where height drops below 7 feet cannot be counted as GLA — report it as NSFA (Nonstandard Finished Area) if finished, or exclude entirely if unfinished. Your sketch should clearly delineate the GLA zone from the NSFA zone."),
        ("Walk-out basement", "Even a fully finished, walk-out basement with full windows and exterior access is below grade and cannot be included in GLA under ANSI. Report the finished area in the Below-Grade Finished Area field. Make a note in the sketch and report explaining the below-grade treatment."),
        ("Cape Cod style — second floor", "Typical Cape Cods have partial second floors with sloped ceilings. Apply the 7-foot rule room by room. The knee wall areas almost certainly fail — only the central portion with full ceiling height counts as second-floor GLA. This often results in less GLA than public records show."),
        ("Split-level homes", "Apply the threshold method: 'below grade' is all finished/unfinished area below the threshold of the front door. Report consistently for both subject and all comps. Tax records for split-levels are notoriously unreliable — measure everything yourself."),
        ("Three-decker / triple-decker", "Multi-family properties are measured as Gross Building Area (GBA) using exterior measurements, not GLA. Below-grade finished area is included in GBA for multi-family. Report each unit's rentable area as part of the GBA calculation."),
        ("Bonus room over garage", "If directly accessible from the main living area and finished with heat/cooling and 7-foot ceiling height, can qualify as GLA. If accessible only from the garage or exterior, typically does not qualify. Verify local market treatment and document your methodology."),
        ("GLA differs from public record (>10%)", "Common in New England due to old, inaccurate assessor data. Document your measurements, note the discrepancy, and explain the likely cause (unfinished attic included in public records, addition not captured, ANSI methodology vs assessor methodology). UAD 3.6 has a specific field for documenting GLA discrepancies from public records."),
    ]
    for title, detail in ne_scenarios:
        with st.expander(f"🏠 {title}"):
            st.write(detail)

    st.divider()
    st.markdown("### NSFA — Nonstandard Finished Area")
    st.markdown("""
NSFA is finished space that does not qualify as GLA under ANSI but still contributes to the utility and value of the property. UAD 3.6 has a dedicated field for NSFA — it is no longer acceptable to either include this space in GLA or omit it entirely.

**Common NSFA examples:**
- Finished attic area where more than half the space is under 7 ft ceiling height
- Finished bonus rooms with ceiling height between 5 and 7 feet
- Areas accessible only through unfinished space

**How to report NSFA:**
1. Measure and record the NSFA square footage separately
2. Note why it fails ANSI in the designated comment field (e.g. "sloping ceiling — less than 7 ft over more than half the area")
3. Reflect NSFA clearly in your sketch — use a distinct hatching or label
4. Address contributory value of NSFA in the sales comparison approach narrative
    """)

    st.caption("Source: ANSI Z765-2021, Appendix F-1 URAR Reference Guide, GSE Inspection and Reporting Tips.")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 6 — INSPECTION CHECKLIST
# ══════════════════════════════════════════════════════════════════════════════
elif selection == "✅ Inspection Checklist":
    st.subheader("UAD 3.6 Inspection Checklist")
    st.markdown("A room-by-room reference for what to collect at every inspection. Print or reference on your mobile device.")
    st.caption("This checklist covers the new and changed data requirements under UAD 3.6. Standard inspection practices remain unchanged.")

    st.markdown("### Before you arrive")
    pre_items = [
        "Pull property from public records — confirm address, legal description, zoning, lot size",
        "Review MLS listing for listed features, updates, and seller disclosures",
        "Check FCC Broadband Map (broadbandmap.fcc.gov) for broadband availability",
        "Confirm assignment type — interior, exterior, or desktop — determines which sections activate",
        "Review prior appraisal if available — note any prior condition or quality ratings",
    ]
    for i, item in enumerate(pre_items):
        st.checkbox(item, key=f"pre_{i}")

    st.divider()
    st.markdown("### Equipment checklist")
    equip_items = [
        "Laser distance measurer (required for ceiling heights)",
        "Mobile device with UAD 3.6 software loaded and assignment open",
        "Camera — front, rear, street scene, all rooms, kitchen close-up, bath close-up",
        "Measuring wheel or laser for exterior measurements",
    ]
    for i, item in enumerate(equip_items):
        st.checkbox(item, key=f"equip_{i}")

    st.divider()
    st.markdown("### Site observations")
    site_items = [
        "Access road type — public paved / private paved / gravel / dirt / other",
        "Site influence — for each influence: onsite / bordering / distant AND positive / neutral / negative",
        "Flood zone — confirm via FEMA map, note zone designation",
        "Zoning — verify current zoning, note any nonconforming use",
        "Utilities — public or private for each: electric, gas, water, sewer",
        "Outbuildings — if present: type, size, utilities extended to each",
        "Disaster mitigation features — storm shutters, hurricane straps, flood vents, seismic retrofit",
        "ADU — if present: separate entrance? kitchen? bed/bath count? legal permit status?",
    ]
    for i, item in enumerate(site_items):
        st.checkbox(item, key=f"site_{i}")

    st.divider()
    st.markdown("### Exterior observations")
    ext_items = [
        "Exterior quality rating (Q1–Q6) — assess independently of interior",
        "Exterior condition rating (C1–C6) — assess independently of interior",
        "Siding material and condition",
        "Roof material, design, and estimated replacement date (ask owner/agent if not observable)",
        "Foundation type and any visible deficiencies",
        "Windows and doors — material, condition, any issues",
        "Trim and architectural detail — quality of finish",
        "Driveway, walkways, patios — material and condition",
        "Any exterior deficiencies — note location, description, impact, estimated repair cost",
    ]
    for i, item in enumerate(ext_items):
        st.checkbox(item, key=f"ext_{i}")

    st.divider()
    st.markdown("### Interior observations — per floor")
    int_items = [
        "Ceiling height — measure each level with laser (required every inspection)",
        "Identify any NSFA areas — sloped ceilings under 7 ft, bonus rooms, etc. Measure separately",
        "Interior quality rating (Q1–Q6) — assess independently of exterior",
        "Interior condition rating (C1–C6) — assess independently of exterior",
        "Flooring materials — type and condition by area",
        "Wall and ceiling materials — type and condition",
        "Trim and millwork — quality and condition",
        "Built-ins, cabinetry quality throughout",
        "HVAC — type, age if observable, condition",
        "Electrical — panel type, any visible issues",
        "Plumbing — any visible issues, water heater age",
        "Any interior deficiencies — note location, description, impact, estimated repair cost",
    ]
    for i, item in enumerate(int_items):
        st.checkbox(item, key=f"int_{i}")

    st.divider()
    st.markdown("### Kitchen details — complete for EACH kitchen")
    kitchen_items = [
        "Update status — updated / not updated / remodeled",
        "Approximate year of update (if updated or remodeled)",
        "Kitchen condition rating (C1–C6)",
        "Brief description — countertop material, cabinet quality, appliances, floor",
    ]
    for i, item in enumerate(kitchen_items):
        st.checkbox(item, key=f"kit_{i}")

    st.divider()
    st.markdown("### Bathroom details — complete for EACH bathroom (including half baths)")
    bath_items = [
        "Update status — updated / not updated / remodeled",
        "Approximate year of update (if updated or remodeled)",
        "Bathroom condition rating (C1–C6)",
        "Brief description — fixtures, tile, vanity, condition",
    ]
    for i, item in enumerate(bath_items):
        st.checkbox(item, key=f"bath_{i}")

    st.divider()
    st.markdown("### Before you leave")
    final_items = [
        "Confirm all required photos taken — front, rear, street scene, all rooms, kitchen, all baths",
        "Confirm ceiling heights recorded for all levels",
        "Confirm NSFA areas identified and measured separately if present",
        "Confirm GLA sketch reflects per-floor breakdown",
        "Confirm broadband availability recorded",
        "Confirm access road type recorded",
        "Confirm roof replacement date collected (from owner/agent/permits)",
        "Confirm outbuilding utilities documented if applicable",
        "Confirm ADU section data collected if applicable",
    ]
    for i, item in enumerate(final_items):
        st.checkbox(item, key=f"final_{i}")

    st.info("💡 Note: This checklist covers UAD 3.6 specific requirements. Standard inspection practices (property access, scope of work, USPAP compliance) remain unchanged.")

    st.divider()
    st.markdown("### 🖨️ Printable Version")
    st.caption("Download as PDF (print-ready) or HTML (open in browser and print). Both formatted for 8.5 x 11 with pen-friendly checkboxes.")

    def make_checklist_pdf():
        import io
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.units import inch
        from reportlab.lib import colors
        from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                        HRFlowable, Table, TableStyle)
        from reportlab.lib.styles import ParagraphStyle
        from reportlab.lib.enums import TA_CENTER
        from reportlab.platypus import Flowable

        class Checkbox(Flowable):
            def __init__(self, size=9):
                Flowable.__init__(self)
                self.size = size
                self.width = size
                self.height = size
            def draw(self):
                self.canv.setLineWidth(1.2)
                self.canv.rect(0, 0, self.size, self.size)

        buf = io.BytesIO()
        doc = SimpleDocTemplate(buf, pagesize=letter,
            leftMargin=0.75*inch, rightMargin=0.75*inch,
            topMargin=0.75*inch, bottomMargin=0.75*inch)

        title_style   = ParagraphStyle("title", fontSize=15, fontName="Helvetica-Bold", spaceAfter=2)
        sub_style     = ParagraphStyle("sub",   fontSize=8,  fontName="Helvetica",
                                       textColor=colors.HexColor("#555555"), spaceAfter=10)
        section_style = ParagraphStyle("sec",   fontSize=10, fontName="Helvetica-Bold",
                                       spaceBefore=10, spaceAfter=4)
        item_style    = ParagraphStyle("item",  fontSize=9,  fontName="Helvetica", leading=13, leftIndent=4)
        footer_style  = ParagraphStyle("foot",  fontSize=7.5, fontName="Helvetica",
                                       textColor=colors.HexColor("#888888"), alignment=TA_CENTER)

        checklist_sections = [
            ("Before You Arrive", [
                "Pull property from public records — confirm address, legal description, zoning, lot size",
                "Review MLS listing for listed features, updates, and seller disclosures",
                "Check FCC Broadband Map (broadbandmap.fcc.gov) for broadband availability",
                "Confirm assignment type — interior, exterior, or desktop — determines which sections activate",
                "Review prior appraisal if available — note any prior condition or quality ratings",
            ]),
            ("Equipment Checklist", [
                "Laser distance measurer (required for ceiling heights)",
                "Mobile device with UAD 3.6 software loaded and assignment open",
                "Camera — front, rear, street scene, all rooms, kitchen close-up, bath close-up",
                "Measuring wheel or laser for exterior measurements",
            ]),
            ("Site Observations", [
                "Access road type — public paved / private paved / gravel / dirt / other",
                "Site influence — for each influence: onsite / bordering / distant AND positive / neutral / negative",
                "Flood zone — confirm via FEMA map, note zone designation",
                "Zoning — verify current zoning, note any nonconforming use",
                "Utilities — public or private for each: electric, gas, water, sewer",
                "Outbuildings — if present: type, size, utilities extended to each",
                "Disaster mitigation features — storm shutters, hurricane straps, flood vents, seismic retrofit",
                "ADU — if present: separate entrance? kitchen? bed/bath count? legal permit status?",
            ]),
            ("Exterior Observations", [
                "Exterior quality rating (Q1-Q6) — assess independently of interior",
                "Exterior condition rating (C1-C6) — assess independently of interior",
                "Siding material and condition",
                "Roof material, design, and estimated replacement date (ask owner/agent if not observable)",
                "Foundation type and any visible deficiencies",
                "Windows and doors — material, condition, any issues",
                "Trim and architectural detail — quality of finish",
                "Driveway, walkways, patios — material and condition",
                "Any exterior deficiencies — note location, description, impact, estimated repair cost",
            ]),
            ("Interior Observations — Per Floor", [
                "Ceiling height — measure each level with laser (required every inspection)",
                "Identify any NSFA areas — sloped ceilings under 7 ft, bonus rooms, etc. Measure separately",
                "Interior quality rating (Q1-Q6) — assess independently of exterior",
                "Interior condition rating (C1-C6) — assess independently of exterior",
                "Flooring materials — type and condition by area",
                "Wall and ceiling materials — type and condition",
                "Trim and millwork — quality and condition",
                "Built-ins, cabinetry quality throughout",
                "HVAC — type, age if observable, condition",
                "Electrical — panel type, any visible issues",
                "Plumbing — any visible issues, water heater age",
                "Any interior deficiencies — note location, description, impact, estimated repair cost",
            ]),
            ("Kitchen Details — Complete for EACH Kitchen", [
                "Update status — updated / not updated / remodeled",
                "Approximate year of update (if updated or remodeled)",
                "Kitchen condition rating (C1-C6)",
                "Brief description — countertop material, cabinet quality, appliances, floor",
            ]),
            ("Bathroom Details — Complete for EACH Bathroom (including half baths)", [
                "Update status — updated / not updated / remodeled",
                "Approximate year of update (if updated or remodeled)",
                "Bathroom condition rating (C1-C6)",
                "Brief description — fixtures, tile, vanity, condition",
            ]),
            ("Before You Leave", [
                "Confirm all required photos taken — front, rear, street scene, all rooms, kitchen, all baths",
                "Confirm ceiling heights recorded for all levels",
                "Confirm NSFA areas identified and measured separately if present",
                "Confirm GLA sketch reflects per-floor breakdown",
                "Confirm broadband availability recorded",
                "Confirm access road type recorded",
                "Confirm roof replacement date collected (from owner/agent/permits)",
                "Confirm outbuilding utilities documented if applicable",
                "Confirm ADU section data collected if applicable",
            ]),
        ]

        story = []
        story.append(Paragraph("UAD 3.6 Inspection Checklist", title_style))
        story.append(Paragraph(
            "Absolute Value Management &amp; A-Tech Appraisal Co.  |  Mandatory: November 2, 2026",
            sub_style))
        story.append(HRFlowable(width="100%", thickness=1,
                                color=colors.HexColor("#cccccc"), spaceAfter=6))
        for sec_title, items in checklist_sections:
            story.append(Paragraph(sec_title, section_style))
            for item in items:
                row = Table([[Checkbox(9), Paragraph(item, item_style)]], colWidths=[18, None])
                row.setStyle(TableStyle([
                    ("VALIGN",        (0,0), (-1,-1), "TOP"),
                    ("LEFTPADDING",   (0,0), (-1,-1), 0),
                    ("RIGHTPADDING",  (0,0), (-1,-1), 0),
                    ("TOPPADDING",    (0,0), (-1,-1), 2),
                    ("BOTTOMPADDING", (0,0), (-1,-1), 2),
                ]))
                story.append(row)
            story.append(HRFlowable(width="100%", thickness=0.5,
                                    color=colors.HexColor("#e0e0e0"),
                                    spaceBefore=6, spaceAfter=2))
        story.append(Spacer(1, 10))
        story.append(Paragraph(
            "This checklist covers UAD 3.6 specific requirements. "
            "Standard inspection practices and USPAP obligations remain unchanged.",
            footer_style))
        doc.build(story)
        buf.seek(0)
        return buf.read()

    printable_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>UAD 3.6 Inspection Checklist</title>
<style>
  body { font-family: Arial, sans-serif; font-size: 11pt; margin: 0.75in; color: #111; }
  h1 { font-size: 15pt; margin-bottom: 2px; }
  .subtitle { font-size: 9pt; color: #555; margin-bottom: 16px; }
  h2 { font-size: 11pt; margin-top: 18px; margin-bottom: 6px; border-bottom: 1px solid #ccc; padding-bottom: 3px; }
  .item { display: flex; align-items: flex-start; margin: 5px 0; }
  .box { width: 13px; height: 13px; border: 1.5px solid #333; display: inline-block; margin-right: 8px; margin-top: 2px; flex-shrink: 0; }
  .label { line-height: 1.4; }
  .footer { font-size: 8pt; color: #888; margin-top: 24px; border-top: 1px solid #ddd; padding-top: 6px; }
  @media print { body { margin: 0.6in; } h2 { page-break-after: avoid; } }
</style>
</head>
<body>
<h1>UAD 3.6 Inspection Checklist</h1>
<div class="subtitle">Presented by Absolute Value Management &amp; A-Tech Appraisal Co. &nbsp;|&nbsp; Mandatory: November 2, 2026</div>
<h2>Before You Arrive</h2>
<div class="item"><span class="box"></span><span class="label">Pull property from public records — confirm address, legal description, zoning, lot size</span></div>
<div class="item"><span class="box"></span><span class="label">Review MLS listing for listed features, updates, and seller disclosures</span></div>
<div class="item"><span class="box"></span><span class="label">Check FCC Broadband Map (broadbandmap.fcc.gov) for broadband availability</span></div>
<div class="item"><span class="box"></span><span class="label">Confirm assignment type — interior, exterior, or desktop — determines which sections activate</span></div>
<div class="item"><span class="box"></span><span class="label">Review prior appraisal if available — note any prior condition or quality ratings</span></div>
<h2>Equipment Checklist</h2>
<div class="item"><span class="box"></span><span class="label">Laser distance measurer (required for ceiling heights)</span></div>
<div class="item"><span class="box"></span><span class="label">Mobile device with UAD 3.6 software loaded and assignment open</span></div>
<div class="item"><span class="box"></span><span class="label">Camera — front, rear, street scene, all rooms, kitchen close-up, bath close-up</span></div>
<div class="item"><span class="box"></span><span class="label">Measuring wheel or laser for exterior measurements</span></div>
<h2>Site Observations</h2>
<div class="item"><span class="box"></span><span class="label">Access road type — public paved / private paved / gravel / dirt / other</span></div>
<div class="item"><span class="box"></span><span class="label">Site influence — for each influence: onsite / bordering / distant AND positive / neutral / negative</span></div>
<div class="item"><span class="box"></span><span class="label">Flood zone — confirm via FEMA map, note zone designation</span></div>
<div class="item"><span class="box"></span><span class="label">Zoning — verify current zoning, note any nonconforming use</span></div>
<div class="item"><span class="box"></span><span class="label">Utilities — public or private for each: electric, gas, water, sewer</span></div>
<div class="item"><span class="box"></span><span class="label">Outbuildings — if present: type, size, utilities extended to each</span></div>
<div class="item"><span class="box"></span><span class="label">Disaster mitigation features — storm shutters, hurricane straps, flood vents, seismic retrofit</span></div>
<div class="item"><span class="box"></span><span class="label">ADU — if present: separate entrance? kitchen? bed/bath count? legal permit status?</span></div>
<h2>Exterior Observations</h2>
<div class="item"><span class="box"></span><span class="label">Exterior quality rating (Q1-Q6) — assess independently of interior</span></div>
<div class="item"><span class="box"></span><span class="label">Exterior condition rating (C1-C6) — assess independently of interior</span></div>
<div class="item"><span class="box"></span><span class="label">Siding material and condition</span></div>
<div class="item"><span class="box"></span><span class="label">Roof material, design, and estimated replacement date (ask owner/agent if not observable)</span></div>
<div class="item"><span class="box"></span><span class="label">Foundation type and any visible deficiencies</span></div>
<div class="item"><span class="box"></span><span class="label">Windows and doors — material, condition, any issues</span></div>
<div class="item"><span class="box"></span><span class="label">Trim and architectural detail — quality of finish</span></div>
<div class="item"><span class="box"></span><span class="label">Driveway, walkways, patios — material and condition</span></div>
<div class="item"><span class="box"></span><span class="label">Any exterior deficiencies — note location, description, impact, estimated repair cost</span></div>
<h2>Interior Observations — Per Floor</h2>
<div class="item"><span class="box"></span><span class="label">Ceiling height — measure each level with laser (required every inspection)</span></div>
<div class="item"><span class="box"></span><span class="label">Identify any NSFA areas — sloped ceilings under 7 ft, bonus rooms, etc. Measure separately</span></div>
<div class="item"><span class="box"></span><span class="label">Interior quality rating (Q1-Q6) — assess independently of exterior</span></div>
<div class="item"><span class="box"></span><span class="label">Interior condition rating (C1-C6) — assess independently of exterior</span></div>
<div class="item"><span class="box"></span><span class="label">Flooring materials — type and condition by area</span></div>
<div class="item"><span class="box"></span><span class="label">Wall and ceiling materials — type and condition</span></div>
<div class="item"><span class="box"></span><span class="label">Trim and millwork — quality and condition</span></div>
<div class="item"><span class="box"></span><span class="label">Built-ins, cabinetry quality throughout</span></div>
<div class="item"><span class="box"></span><span class="label">HVAC — type, age if observable, condition</span></div>
<div class="item"><span class="box"></span><span class="label">Electrical — panel type, any visible issues</span></div>
<div class="item"><span class="box"></span><span class="label">Plumbing — any visible issues, water heater age</span></div>
<div class="item"><span class="box"></span><span class="label">Any interior deficiencies — note location, description, impact, estimated repair cost</span></div>
<h2>Kitchen Details — Complete for EACH Kitchen</h2>
<div class="item"><span class="box"></span><span class="label">Update status — updated / not updated / remodeled</span></div>
<div class="item"><span class="box"></span><span class="label">Approximate year of update (if updated or remodeled)</span></div>
<div class="item"><span class="box"></span><span class="label">Kitchen condition rating (C1-C6)</span></div>
<div class="item"><span class="box"></span><span class="label">Brief description — countertop material, cabinet quality, appliances, floor</span></div>
<h2>Bathroom Details — Complete for EACH Bathroom (including half baths)</h2>
<div class="item"><span class="box"></span><span class="label">Update status — updated / not updated / remodeled</span></div>
<div class="item"><span class="box"></span><span class="label">Approximate year of update (if updated or remodeled)</span></div>
<div class="item"><span class="box"></span><span class="label">Bathroom condition rating (C1-C6)</span></div>
<div class="item"><span class="box"></span><span class="label">Brief description — fixtures, tile, vanity, condition</span></div>
<h2>Before You Leave</h2>
<div class="item"><span class="box"></span><span class="label">Confirm all required photos taken — front, rear, street scene, all rooms, kitchen, all baths</span></div>
<div class="item"><span class="box"></span><span class="label">Confirm ceiling heights recorded for all levels</span></div>
<div class="item"><span class="box"></span><span class="label">Confirm NSFA areas identified and measured separately if present</span></div>
<div class="item"><span class="box"></span><span class="label">Confirm GLA sketch reflects per-floor breakdown</span></div>
<div class="item"><span class="box"></span><span class="label">Confirm broadband availability recorded</span></div>
<div class="item"><span class="box"></span><span class="label">Confirm access road type recorded</span></div>
<div class="item"><span class="box"></span><span class="label">Confirm roof replacement date collected (from owner/agent/permits)</span></div>
<div class="item"><span class="box"></span><span class="label">Confirm outbuilding utilities documented if applicable</span></div>
<div class="item"><span class="box"></span><span class="label">Confirm ADU section data collected if applicable</span></div>
<div class="footer">UAD 3.6 Inspection Checklist &nbsp;|&nbsp; Absolute Value Management &amp; A-Tech Appraisal Co. &nbsp;|&nbsp; Mandatory November 2, 2026</div>
</body>
</html>"""

    dl_col1, dl_col2 = st.columns(2)
    with dl_col1:
        if REPORTLAB_AVAILABLE:
            st.download_button(
                label="📄 Download PDF Checklist",
                data=make_checklist_pdf(),
                file_name="UAD_36_Inspection_Checklist.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        else:
            st.warning("Add `reportlab` to requirements.txt to enable PDF download.")
    with dl_col2:
        st.download_button(
            label="🌐 Download HTML Checklist",
            data=printable_html,
            file_name="UAD_36_Inspection_Checklist.html",
            mime="text/html",
            use_container_width=True
        )

# ══════════════════════════════════════════════════════════════════════════════
# TAB 7 — FAQ / REVISION RESPONSES
# ══════════════════════════════════════════════════════════════════════════════
elif selection == "❓ FAQ / Revision Responses":
    st.subheader("FAQ & Common Revision Responses")
    st.markdown("Common questions from lenders, AMCs, and underwriters during the UAD 3.6 transition — with suggested appraiser responses.")

    faq_search = st.text_input("🔍 Search FAQs", placeholder="e.g. 1004MC, ceiling height, comp drive-by...")

    faqs = [
        ("Why didn't you use the 1004MC?",
         "Lender or AMC requests the 1004MC form.",
         "The 1004MC form has been retired under UAD 3.6 and does not exist in the redesigned URAR. Market conditions analysis is now incorporated directly into the URAR Market section using structured data fields, consistent with the requirements of the Uniform Appraisal Dataset 3.6 and the redesigned Uniform Residential Appraisal Report. The market conditions analysis contained within this report satisfies the same analytical obligations previously addressed by the 1004MC."),
        ("Why is your GLA different from the tax record?",
         "Lender questions GLA discrepancy from public records.",
         "The gross living area reported in this appraisal is based on field measurements conducted in accordance with ANSI Z765-2021 measurement standards as required under UAD 3.6. Discrepancies between appraiser-measured GLA and public record data are not uncommon and are typically attributable to inaccuracies in assessor records, inclusion of non-qualifying areas (such as unfinished attic or basement space) in the public record figure, or improvements completed after the last assessor measurement. The measurements indicated within this report are considered accurate and have been applied consistently to the subject and comparable sales."),
        ("Why didn't you inspect the comparable sales from the street?",
         "AMC or lender notes appraiser did not conduct drive-by comp inspections.",
         "The requirement to physically inspect comparable sales from the street has been retired under UAD 3.6. Per the URAR Reference Guide: 'While we still require clear descriptive color photos of the front of each comparable, we have retired the requirement to inspect the comparable sales from the street.' Front photos of all comparable sales have been provided as required. The data used to verify and select comparables is consistent with the verification standards applicable to UAD 3.6 assignments."),
        ("What is the ceiling height of the subject?",
         "Underwriter requests ceiling height data.",
         "Ceiling height has been documented in the Interior Features section of this report as required under UAD 3.6 (Report Field ID 10.045). [State the ceiling height as measured.] Ceiling height was measured using a laser distance measurer in accordance with ANSI Z765-2021."),
        ("Why does the subject have NSFA listed?",
         "Lender questions Nonstandard Finished Area designation.",
         "The Nonstandard Finished Area (NSFA) designation reflects finished space within the subject property that does not qualify as above-grade gross living area under ANSI Z765-2021. Specifically, [describe the area — e.g. 'the finished area of the upper level where ceiling height falls below 7 feet over more than half the floor area']. ANSI Z765-2021, as incorporated in UAD 3.6, requires that space be excluded from GLA when ceiling height does not meet the 7-foot threshold over the majority of the area. This space has been reported separately in the designated NSFA field and its contributory value has been addressed in the sales comparison analysis."),
        ("Why are there separate Exterior and Interior condition ratings?",
         "Lender unfamiliar with the new 3.6 condition rating structure.",
         "Under UAD 3.6, condition is reported at three levels: Exterior Condition, Interior Condition, and Overall Condition. This structure replaces the single condition rating used in UAD 2.6 and provides greater transparency into the physical state of the property. The Overall Condition rating is the reconciliation of the Exterior and Interior ratings and serves the same function as the condition rating in prior report formats. All three ratings have been assigned and are consistent with the physical observations documented throughout this report."),
        ("Why isn't there an Updated / Not Updated / Remodeled designation for the kitchen?",
         "Lender looking for the old kitchen update checkbox.",
         "The 'Updated / Not Updated / Remodeled' designation for kitchens and bathrooms has been retired under UAD 3.6. This has been replaced by the Kitchen Details section, which captures update status, approximate year of update, condition rating, and a brief description for each kitchen individually. This information is contained in the Kitchen Details section of this report and provides more specific and actionable data than the prior checkbox format."),
        ("Please provide the broadband availability for the subject.",
         "Lender or AMC requests broadband data.",
         "Broadband internet availability for the subject property has been documented in the Site section of this report as required under UAD 3.6. [State the broadband status as reported.] This information was verified via the FCC Broadband Map and/or confirmed with the property owner/listing agent at the time of inspection."),
        ("Why does the appraised value exceed the predominant neighborhood value?",
         "Underwriter questions value above neighborhood range — common for coastal or unique properties.",
         "The predominant value range stated in this report reflects the broader marketing area as a whole. The subject property's location, physical characteristics, and features position it at the upper end of the market segment, and homes of similar quality and utility within this area support a value conclusion above the predominant range. The comparable sales selected reflect properties most competitive with the subject in terms of location, GLA, quality, and condition, and the adjusted value indications are consistent with the appraised value. The subject is not considered to be over-improved for its marketing area."),
        ("Can you provide the time adjustment support?",
         "Lender or AMC requests time adjustment documentation — especially relevant post-1004MC.",
         "Time adjustments in this report are supported by market data analysis contained in the Market Conditions section of the URAR. [Reference your specific supporting data — e.g. paired sales analysis, median price trend data, DOM trends, list-to-sale price ratios.] As the 1004MC form has been retired under UAD 3.6, market conditions support is now incorporated directly into the report's structured Market section, which contains the analytical basis for all time adjustments applied."),
    ]

    if faq_search:
        q = faq_search.lower()
        filtered_faqs = [f for f in faqs if
                         q in f[0].lower() or q in f[1].lower() or q in f[2].lower()]
    else:
        filtered_faqs = faqs

    st.write(f"**{len(filtered_faqs)} entr{'y' if len(filtered_faqs)==1 else 'ies'}**")
    st.divider()

    for idx, (question, trigger, response) in enumerate(filtered_faqs):
        with st.expander(f"❓ {question}"):
            st.caption(f"🔔 Trigger: {trigger}")
            st.markdown("**Suggested response:**")
            st.text_area("Copy:", value=response, height=160, key=f"faq_{idx}")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 8 — SOFTWARE & TOOLS
# ══════════════════════════════════════════════════════════════════════════════
elif selection == "💻 Software & Tools":
    st.subheader("Report Writing Software & Tools")
    st.markdown("A plain-language guide to the software landscape for UAD 3.6 — written for appraisers at every experience level.")

    st.markdown("### The two categories of report-writing software")

    col_trad, col_ai = st.columns(2)
    with col_trad:
        st.markdown("#### Traditional platforms")
        st.caption("e.g. TOTAL by a la mode, ClickForms, ACI Sky")
        st.write("These have been the industry standard for decades. You enter data manually, build your report field by field, and write narrative addenda. They are being updated for UAD 3.6. TOTAL for Mobile is a la mode's push toward mobile-first data collection.")
        st.markdown("""
✅ Full control over every field  
✅ Deep MLS and data source integration  
✅ Established — accepted by all AMCs and lenders  
✅ Large user community and training resources  
❌ UAD 3.6 transition still rolling out  
❌ Monthly subscription cost  
❌ Office-based workflow less suited to new field data requirements  
        """)

    with col_ai:
        st.markdown("#### AI-assisted platforms")
        st.caption("e.g. Automax, Aivre, ApprAIz, Bradford")
        st.write("A new generation of tools built from the ground up for UAD 3.6. Use AI to auto-populate fields, generate sketches, suggest comps, and flag compliance issues in real time. Both Automax and Aivre were featured at the 2026 UAD 3.6 Bootcamp alongside Fannie Mae and Freddie Mac.")
        st.markdown("""
✅ Built for UAD 3.6 from day one  
✅ Faster structured data entry in the field  
✅ Real-time UCDP compliance checking  
✅ Auto-populates many required fields  
❌ Newer — less established track record  
❌ AMC and lender acceptance varies  
❌ Workflow change requires adjustment period  
        """)

    st.divider()
    st.markdown("### What AI actually does in appraisal software")
    st.caption("Plain-language explanation — no hype")

    ai_items = [
        ("🤖 Computer vision / scanning", "You walk through a property with your phone and the app uses the camera to measure rooms, generate a sketch, and identify features — flooring type, ceiling height, condition indicators. Some platforms do this in real time during the inspection walkthrough."),
        ("🤖 Auto-population", "The software pulls property data from public records, MLS, and other sources and pre-fills report fields — address, lot size, year built, zoning, etc. — so it's already there when you open the assignment."),
        ("🤖 Comp suggestion", "Algorithms scan MLS and public record data and suggest comparable sales based on proximity, size, age, condition, and other factors. You still select and verify every comp — the AI narrows the search, you make the professional judgment."),
        ("🤖 Compliance checking", "The software flags UAD 3.6 rule violations in real time before you submit — missing required fields, inconsistent C/Q ratings, data that doesn't pass UCDP logic rules. Catches errors before the reviewer does."),
        ("⚠️ What AI does NOT do", "AI does not form the opinion of value. The analysis, judgment, reconciliation, and professional conclusions are entirely yours. USPAP places that responsibility on the appraiser — no software product changes that, and no lender or AMC can accept an AI-formed value opinion."),
    ]

    for title, detail in ai_items:
        with st.expander(title):
            st.write(detail)

    st.divider()
    st.markdown("### Automax vs Aivre — balanced overview")
    st.caption("Both were featured as UAD 3.6 demo software at the 2026 Appraiser eLearning Bootcamp alongside Fannie Mae and Freddie Mac.")

    col_am, col_av = st.columns(2)
    with col_am:
        st.markdown("#### Automax")
        st.caption("Free with hybrid network participation — or subscription without")
        st.write("Automax offers the platform free in exchange for participation in their hybrid appraisal order network. If you prefer to use it without joining the network, a subscription option is available. Hybrid orders typically involve a reduced-scope inspection with the appraiser completing the desktop or hybrid valuation. Order acceptance is generally flexible.")
        st.markdown("""
**Features include:**
- Instant sketch generation — built-in, similar to CubiCasa but instant in the report
- MLS + public records + Zillow comp data
- Comparable selection and report tools (similar functionality to Spark and TruTracts)
- TOTAL data integration (UAD 2.6 now, 3.6 on active roadmap)
- Cloud workfile storage — USPAP compliant
- Opt-in data sharing network

**Best for:** Appraisers who want to reduce software overhead and are open to hybrid assignments, or those who want an all-in-one platform and prefer to subscribe independently.

**Note:** Automax's UAD 3.6 deployment is on their active roadmap — confirm current status directly with Automax before committing.
        """)
        st.link_button("▶ Watch Demo — UAD 3.6 in Minutes (Storyboard EMP)", "https://www.bigmarker.com/Storyboard-EMP/copilot-to-the-future-uad-3-6-appraisals-in-minutes")

    with col_av:
        st.markdown("#### Aivre")
        st.caption("Currently free — subscription pricing coming")
        st.write("Aivre was the first GSE-verified platform for UAD 3.6, verified by both Fannie Mae and Freddie Mac before any other vendor. The platform is currently free while in its launch phase — subscription pricing has been announced but not yet implemented. This is a limited window to try it at no cost.")
        st.markdown("""
**Features include:**
- First GSE-verified UAD 3.6 platform (Fannie Mae + Freddie Mac verified)
- MLS and public records integration — auto-populates property data
- Comparable selection and analytics tools (similar functionality to Spark and TruTracts)
- UAD-compliant language auto-formatting
- Photo classification and AI-assisted data entry
- Real-time UCDP compliance checking via the UAD Compliance API
- Early testing shows 3+ hours saved per report and ~30% fewer revisions
- No order network obligations — fully standalone

**Best for:** Appraisers who want the most UAD 3.6-native platform available and want to try it while it's still free.

**Note:** No sketch tool currently — verify current feature set as this space moves fast. Subscription pricing is coming — get in now while it's free.
        """)
        st.link_button("▶ Watch Demo — Appraisal Update Podcast (3.3.26)", "https://www.youtube.com/watch?v=8UkctnGKCRE&t=541s")
        st.link_button("▶ Watch Demo — Aivre Walkthrough Webinar", "https://www.youtube.com/watch?v=u-iKQZmmM6M&t=1261s")

    st.divider()
    st.markdown("### Software demo videos — watch before you decide")
    st.caption("These videos show real workflows in real software — the fastest way to evaluate before committing.")

    demos = [
        ("TOTAL by a la mode", "Live Demo: How to use UAD 3.6 within TOTAL (Storyboard EMP)", "https://www.youtube.com/watch?v=YlbaS_iKCI4", "Storyboard EMP hosted this live demo showing the full UAD 3.6 workflow in TOTAL, the most widely used traditional platform. Good starting point if you're a current TOTAL user."),
        ("Aivre", "The Appraisal Update Podcast — UAD 3.6 and AI: How Aivre Is Changing Appraisers' Workflows (3.3.26)", "https://www.youtube.com/watch?v=8UkctnGKCRE&t=541s", "Bryan Reynolds and Aivre CEO Jake Lew walk through the software live, including a screen-share demo. The most current look at Aivre's UAD 3.6 workflow."),
        ("Aivre", "Aivre Appraisal Software Walkthrough Webinar — UAD 3.6, AI & Automation for Appraisers", "https://www.youtube.com/watch?v=u-iKQZmmM6M&t=1261s", "Full platform walkthrough webinar. Covers data entry, photo classification, analytics, and compliance checking in detail."),
        ("Automax", "Webinar: Copilot to the Future — UAD 3.6 in Minutes (Storyboard EMP)", "https://www.bigmarker.com/Storyboard-EMP/copilot-to-the-future-uad-3-6-appraisals-in-minutes", "Automax's UAD 3.6 demo webinar hosted by Storyboard EMP. Shows how Automax handles the full report workflow including instant sketch generation."),
        ("SFREP / Appraise-It Pro", "Writing a UAD 3.6 Report in Appraise-It Pro", "https://www.youtube.com/watch?v=w0xgZugiSTA&t=1761s", "SFREP walks through the UAD 3.6 dynamic URAR in Appraise-It Pro. SFREP was the first of the 'big four' platforms to obtain GSE verification. Free 6-month trial available at sfrep.com."),
        ("SFREP / Appraise-It Pro", "Appraise-It Pro UAD 3.6 — Additional Demo", "https://www.youtube.com/watch?v=TFWlwfl1Ycc", "Second SFREP demo covering additional UAD 3.6 functionality in Appraise-It Pro."),
        ("ACI", "UAD 3.6 and ACI Solutions — Hosted by NAN", "https://www.youtube.com/watch?v=udVnaQXjLyU&t=1852s", "Nationwide Appraisal Network hosted this webinar with ACI covering how their platform handles UAD 3.6 compliance, ordering, and delivery."),
    ]

    for software, title, url, desc in demos:
        with st.expander(f"▶ {software} — {title}"):
            st.write(desc)
            st.link_button(f"Watch: {title}", url)

    st.divider()
    st.info("**A note for newer appraisers:** AI-assisted platforms speed up data collection and flag compliance issues, but they work best in the hands of someone who understands what the fields mean, why certain adjustments are made, and what USPAP requires. Learn the process first — the technology amplifies it, it doesn't replace it.")

    st.caption("Source: Appraiser eLearning 2026 UAD 3.6 Bootcamp, Storyboard EMP, Working RE, McKissock Learning, Fannie Mae Appraiser Update (Jan 2026), Aivre press release (Oct 2025).")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 9 — TRAINING RESOURCES
# ══════════════════════════════════════════════════════════════════════════════
elif selection == "📚 Training Resources":
    st.subheader("Training Resources & Reference Materials")
    st.markdown("The best UAD 3.6 resources — curated and organized so you don't have to hunt across multiple sites.")

    st.markdown("### 📋 Start here — free GSE resources")

    gse_items = [
        ("📄 Appendix F-1: URAR Reference Guide", "https://singlefamily.fanniemae.com/media/document/zip/appendix-f-1-urar-reference-guide", "The authoritative field-by-field reference for the new URAR. Download includes the PDF reference guide (375 pages) AND the Excel field mapping file. If you have a question about a specific field, this is the answer. Download it, keep it searchable.", "Fannie Mae — ZIP download (PDF + Excel)"),
        ("📄 UAD Inspection & Reporting Tips", "https://singlefamily.fanniemae.com/media/43946/display", "Published Oct 2025 by Fannie Mae and Freddie Mac. A concise job aid highlighting notable differences in information collected between UAD 2.6 and 3.6. Best quick-reference document for inspection prep — much shorter than Appendix F-1.", "Fannie Mae"),
        ("📄 Sample URAR Scenarios", "https://sf.freddiemac.com/docs/pdf/uad-sample-scenarios-combined.pdf", "Example completed reports showing what a UAD 3.6 URAR actually looks like for different property types — SFR, condo, 2-4 unit, manufactured housing. Essential for understanding what finished reports should contain before you attempt one.", "Freddie Mac — PDF"),
        ("🎬 Fannie Mae UAD 3.6 Training", "https://www.fanniemae.com/course/singlefamily/uadtrainingfiles/story.html", "Free interactive training from Fannie Mae covering the new URAR structure, dynamic form behavior, and key field requirements. Best starting point before attempting your first UAD 3.6 report.", "Fannie Mae — Interactive course"),
        ("📄 Freddie Mac UAD Resources", "https://sf.freddiemac.com/tools-learning/uniform-mortgage-data-program/uad", "Freddie Mac's full resource hub — includes their policy bulletin (2025-7), supplemental guidance, compliance rules, and implementation documents. Some nuances differ from Fannie Mae policy so worth reviewing both.", "Freddie Mac"),
        ("📄 UAD 3.6 FAQ", "https://singlefamily.fanniemae.com/media/23286/display", "Official FAQ from Fannie Mae and Freddie Mac answering the most common implementation questions. Good first stop when you encounter something unexpected in the new report format.", "Fannie Mae & Freddie Mac"),
        ("🗺️ FCC Broadband Map", "https://broadbandmap.fcc.gov/home", "Required for verifying broadband internet availability at the subject property — a new required field in UAD 3.6. Enter the subject address to get the official FCC broadband availability data.", "FCC"),
    ]

    for title, url, desc, source in gse_items:
        with st.expander(title):
            st.write(desc)
            st.caption(f"Source: {source}")
            st.link_button("Open / Download", url)

    st.divider()
    st.markdown("### From Absolute Value Management & A-Tech Appraisal")
    st.info("""
This resource is provided by **Absolute Value Management** and **A-Tech Appraisal Co.** as a service to appraisers navigating the UAD 3.6 transition.

Questions about UAD 3.6 assignments, software compatibility with your current AMC workflow, or transition support? Reach out to your contact at Absolute Value Management.

This guide will be updated as new guidance is released by Fannie Mae and Freddie Mac. Last content review: March 2026.
    """)

    col_f1, col_f2 = st.columns(2)
    with col_f1:
        if os.path.exists(AVM_LOGO):
            st.image(AVM_LOGO, width=140)
    with col_f2:
        if os.path.exists(ATECH_LOGO):
            st.image(ATECH_LOGO, width=140)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 10 — BEFORE YOUR FIRST 3.6 ORDER
# ══════════════════════════════════════════════════════════════════════════════
elif selection == "🚀 Before Your First 3.6 Order":
    st.subheader("🚀 Before Your First UAD 3.6 Order")
    st.markdown("A one-time readiness checklist to run through before you accept your first UAD 3.6 assignment. This is separate from the inspection checklist — this is about making sure you and your workflow are ready before the order even arrives.")
    st.info("You don't need to be perfect before accepting your first order — but you should be deliberate. Running through this once will prevent the most common first-order problems.")

    st.divider()
    st.markdown("### 💻 Software readiness")
    sw_items = [
        ("Confirm your report-writing software has completed GSE verification for UAD 3.6", "Not all platforms are verified yet. Verified platforms as of early 2026: Aivre, SFREP / Appraise-It Pro, TOTAL by a la mode (Launch Edition), ACI. Check your vendor's website for current status before accepting a 3.6 order."),
        ("Download and install the latest software update", "UAD 3.6 support is only available in recent versions. Don't assume your current installation is ready — check for updates."),
        ("Complete at least one practice report in the new format", "Use the GSE's sample scenarios (Appendix D) as your source material. Run through the full workflow — don't skip sections. The goal is to find your first surprise before it's on a live order."),
        ("Set up your templates and QuickLists for the new format", "UAD 3.6 fields only match about 6% of UAD 2.6 fields — your existing templates won't transfer. Build a basic 3.6 template with your standard information before your first order arrives."),
        ("Confirm your mobile app is updated and ready if using mobile workflow", "TOTAL for Mobile, Apex Portal, or whichever mobile solution you're using — make sure it's on the latest version and syncing correctly with your desktop software."),
    ]
    for i, (item, detail) in enumerate(sw_items):
        with st.expander(f"☐ {item}"):
            st.write(detail)

    st.divider()
    st.markdown("### 🔧 Equipment readiness")
    eq_items = [
        ("Purchase a quality laser distance measurer if you don't have one", "Ceiling height is a required field at every inspection under UAD 3.6. A tape measure and ladder is not practical or safe. A quality laser measurer (Leica, Bosch, or similar) typically runs $50-150 and is a one-time investment."),
        ("Test your laser measurer before your first inspection", "Know how to use it quickly and accurately — ceiling measurements at the property are not the time to learn a new tool."),
        ("Confirm your phone/tablet camera meets photo requirements", "UAD 3.6 requires more photos in more specific locations — photos must be placed in the correct section of the report, not dumped into a general addendum. Make sure you have enough storage and a reliable camera."),
    ]
    for i, (item, detail) in enumerate(eq_items):
        with st.expander(f"☐ {item}"):
            st.write(detail)

    st.divider()
    st.markdown("### 📋 Knowledge readiness")
    kn_items = [
        ("Download Appendix F-1 and keep it searchable on your device", "375 pages — you won't memorize it, but you need to be able to search it quickly when you hit an unfamiliar field. Download it now, not mid-report."),
        ("Review the new C and Q rating structure", "You now rate Exterior and Interior separately before reconciling to Overall. Review the C & Q Ratings tab on this site and be clear on how the reconciliation works before your first inspection."),
        ("Understand the new kitchen and bathroom reporting requirements", "Per-kitchen and per-bathroom structured sections replace the old checkbox. Know what you need to collect at each kitchen and bath before you walk into the property."),
        ("Review the new Site Influence field options", "The old View field is gone. The new Site Influence section captures proximity (onsite/bordering/distant) and direction (positive/neutral/negative). Review the Site Influence Guide tab on this site."),
        ("Know how NSFA differs from GLA", "Nonstandard Finished Area must be measured and reported separately. Know the ANSI 7-foot ceiling height rule and how to identify NSFA areas before your first inspection."),
        ("Have the FCC Broadband Map bookmarked", "Broadband availability is a required field. Bookmark broadbandmap.fcc.gov and know how to look up a property address before your first inspection."),
    ]
    for i, (item, detail) in enumerate(kn_items):
        with st.expander(f"☐ {item}"):
            st.write(detail)

    st.divider()
    st.markdown("### 🏦 AMC and lender readiness")
    amc_items = [
        ("Confirm your AMC is ready to receive UAD 3.6 reports", "During the transition period, not all AMCs and lenders are ready to accept 3.6 reports. A completed 3.6 report cannot be converted to 2.6 — if your client can't accept it, you'd need to start over. Confirm before you accept the order."),
        ("Know what format the specific order requires", "Orders during the transition period will specify UAD 2.6 or UAD 3.6. Read the order carefully — don't assume all orders from the same AMC will be the same format."),
        ("Understand what happens if you need more time", "UAD 3.6 reports take longer initially — especially the first few. Communicate proactively with your AMC if you need additional time. Your AMC is here to support the transition, not penalize you for it."),
        ("Know who to contact at your AMC with questions", "Have your AMC contact information handy before your first order. Questions will come up — the best time to establish that communication channel is before you need it urgently."),
    ]
    for i, (item, detail) in enumerate(amc_items):
        with st.expander(f"☐ {item}"):
            st.write(detail)

    st.divider()
    st.success("When you've worked through this checklist you're ready. Your first UAD 3.6 order will still have surprises — that's normal. The goal is to make sure none of them are the preventable ones.")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 11 — SITE INFLUENCE GUIDE
# ══════════════════════════════════════════════════════════════════════════════
elif selection == "🌍 Site Influence Guide":
    st.subheader("🌍 Site Influence Quick Reference Guide")
    st.markdown("The old View field is gone. UAD 3.6 replaces it with a structured Site Influence section that captures two separate dimensions for every influence: **where it is** relative to the property and **whether it's positive, neutral, or negative**.")

    st.info("The Site section is the second largest chapter in Appendix F-1 (30 pages), trailing only the Sales Comparison Approach. Take it seriously — automated review tools will check for consistency between your site influence entries and your adjustments.")

    st.divider()
    st.markdown("### The two dimensions you must report for every influence")

    col_prox, col_dir = st.columns(2)
    with col_prox:
        st.markdown("#### Dimension 1 — Proximity")
        st.markdown("""
**Onsite** — The influence is located on the subject's lot itself.
*Example: A pond on the property, a power line running across the lot, mature trees.*

**Bordering** — The influence is immediately adjacent to the property but not on it.
*Example: A busy road directly bordering the rear lot line, a neighboring commercial property, a stream along the property edge.*

**Distant** — The influence affects value from a distance without direct adjacency.
*Example: A water view from the property, proximity to a highway heard but not adjoining, a golf course visible from the backyard.*
        """)
    with col_dir:
        st.markdown("#### Dimension 2 — Direction")
        st.markdown("""
**Positive** — The influence adds to marketability and value.
*Example: Waterfront location, golf lot, park views, conservation land.*

**Neutral** — The influence has no measurable effect on value.
*Example: Standard residential street, typical neighborhood amenities.*

**Negative** — The influence detracts from marketability and value.
*Example: Power lines, busy road, commercial adjacency, flood zone, industrial proximity.*
        """)

    st.divider()
    st.markdown("### Common scenarios — how to classify them")

    scenarios = [
        ("Waterfront — water on the lot (pond, river, lake)", "Onsite", "Positive", "The water feature is part of the subject's lot. Positive influence on marketability. Support with waterfront comp adjustments in the sales comparison approach."),
        ("Water view — can see water but not on lot", "Distant", "Positive", "The view influence comes from a distance. Still positive but typically commands a lower premium than direct waterfront. Distinguish clearly from onsite water."),
        ("Bordering water — water adjacent to but not on lot", "Bordering", "Positive", "Common with properties backing to a river or stream that runs along the lot line. The water is not on the property but is immediately adjacent."),
        ("Golf lot — fairway or green adjacent to property", "Bordering", "Positive", "Typically borders the lot rather than being on it. Positive influence — note the specific hole or location if relevant to marketability."),
        ("Power lines — crossing or on the lot", "Onsite", "Negative", "Easement running across the property. Negative influence on marketability. Note the easement in the site section and support your adjustment with paired sales or market data."),
        ("Power lines — along adjacent street or bordering", "Bordering", "Negative", "Lines run along the road or neighboring parcel but don't cross the subject lot. Still negative but typically a lesser impact than onsite."),
        ("High traffic road — lot directly borders it", "Bordering", "Negative", "The busy road is immediately adjacent. Negative influence — noise, safety, and marketability impact. Support with paired sales where possible."),
        ("Highway noise — heard but not adjacent", "Distant", "Negative", "Traffic noise from a nearby highway that doesn't directly border the property. Negative but typically lesser than bordering. Note the approximate distance."),
        ("Conservation land / open space — adjacent", "Bordering", "Positive", "Abutting conservation land or open space adds privacy and permanence. Positive influence — common in rural RI/MA markets."),
        ("Commercial property — directly adjacent", "Bordering", "Negative", "Neighboring commercial use creates noise, traffic, and visual impact. Negative influence — note the type of commercial use."),
        ("Flood zone — affects part of the lot", "Onsite", "Negative", "The flood zone designation is a site characteristic of the property itself. Negative influence — note whether improvements are in or out of the flood zone."),
        ("Industrial or manufacturing — nearby but not adjacent", "Distant", "Negative", "Odor, noise, truck traffic from a nearby industrial use. Negative influence at a distance — note approximate distance and nature of the use."),
        ("No notable external influences", "N/A", "Neutral", "If no external influences materially affect the property, report neutral. Don't force a positive or negative when the site is truly typical for the area."),
        ("Coastal location — ocean proximity and views", "Distant or Bordering", "Positive", "Depends on the specific property. Oceanfront (bordering or onsite) vs ocean view property (distant). Classify based on actual proximity. Common in Narragansett, Newport, coastal RI/MA markets."),
    ]

    for scenario, proximity, direction, notes in scenarios:
        icon = "🟢" if direction == "Positive" else "🔴" if direction == "Negative" else "⚪"
        with st.expander(f"{icon} {scenario}"):
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Proximity", proximity)
            with col_b:
                st.metric("Direction", direction)
            st.write(notes)

    st.divider()
    st.markdown("### Key rules to remember")
    rules = [
        "A single property can have multiple site influences — report each one separately.",
        "The proximity and direction classifications must be internally consistent with your adjustments in the sales comparison approach. If you report a negative influence, there should be a corresponding adjustment.",
        "The support for your site influence adjustment should be the same as any other adjustment — paired sales analysis, market data, or documented market knowledge.",
        "When no comparable sales share the same influence (no bracket), document your adjustment methodology clearly. A conservative adjustment based on market knowledge and realtor interviews is acceptable when paired sales aren't available.",
        "Don't overclassify — a standard residential street is neutral, not a negative. Reserve negative classifications for influences that demonstrably affect marketability in your market.",
        "For coastal RI and MA markets: waterfront and water view classifications will be scrutinized. Be precise about proximity and support your adjustments with market data specific to those submarkets.",
    ]
    for rule in rules:
        st.markdown(f"• {rule}")

    st.caption("Source: Appendix F-1 URAR Reference Guide (Fannie Mae, 30-page Site section), GSE Inspection and Reporting Tips (Oct 2025).")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 12 — WORKING WITH YOUR AMC
# ══════════════════════════════════════════════════════════════════════════════
elif selection == "🤝 Working With Your AMC":
    st.subheader("🤝 Working With Your AMC During the UAD 3.6 Transition")
    st.markdown("The transition to UAD 3.6 is a shared process — not something appraisers navigate alone. Your AMC is your partner in this transition, not an obstacle. This section covers what to expect, how to communicate, and how to get help when you need it.")

    st.success("**If you need help, reach out. If you need more time, communicate. We are here to support you through this transition — not to judge you for it.**")

    st.divider()
    st.markdown("### What your AMC needs from you on UAD 3.6 orders")

    needs = [
        ("Confirm you are set up for UAD 3.6 before accepting orders", "Before accepting your first UAD 3.6 order, make sure your software is verified, updated, and that you've completed at least one practice report. If you're not ready yet, let us know — we can route UAD 3.6 orders to appraisers who are ready while you get set up."),
        ("Tell us upfront if an order will take longer than usual", "UAD 3.6 reports take more time initially — especially the first several. This is expected and normal. What we need from you is a heads up before the due date, not an explanation after it. Early communication always results in a better outcome than a late surprise."),
        ("Flag any issues with the report format or lender readiness immediately", "If you complete a UAD 3.6 report and discover the lender can't accept it, contact us right away. A completed 3.6 report cannot be converted to 2.6 — the sooner we know, the more options we have to resolve it."),
        ("Use the correct format for each specific order", "Each order will specify UAD 2.6 or UAD 3.6. Read the order instructions carefully. During the transition period we will have both formats in circulation simultaneously — don't assume all orders from us are the same format."),
        ("Ask questions before you start, not after you submit", "If something about the assignment, format, or scope is unclear, contact us before you begin. Questions after submission often result in revisions that could have been avoided. There are no bad questions during a transition this significant."),
    ]
    for title, detail in needs:
        with st.expander(f"📋 {title}"):
            st.write(detail)

    st.divider()
    st.markdown("### What you can expect from us")

    support = [
        ("We will not penalize you for the learning curve", "UAD 3.6 is the biggest format change in 15 years. We understand that first reports take longer and may have more questions. Our goal is to support your transition, not create a penalty system around it. If your first few 3.6 reports take extra time, communicate with us and we'll work with you."),
        ("We will be clear about which orders require UAD 3.6", "Every order will clearly specify the required format. We will not leave you guessing. If an order is unclear, contact us and we'll clarify before you start."),
        ("We will keep you informed as lender readiness changes", "During the transition period, different lenders are adopting 3.6 at different rates. We will communicate which lenders are 3.6-ready and update you as that changes so you're never caught off guard."),
        ("We will help you resolve format issues", "If a lender cannot accept a 3.6 report you've completed, we will work with you to find the best resolution. We handle the lender and AMC side of that conversation — you focus on the appraisal."),
        ("We will share resources and training as we find them", "This site is part of that commitment. We'll continue to update it as new guidance, tools, and best practices emerge. If you find something useful that isn't here, let us know and we'll add it."),
    ]
    for title, detail in support:
        with st.expander(f"✅ {title}"):
            st.write(detail)

    st.divider()
    st.markdown("### Common transition situations and how to handle them")

    situations = [
        ("I received a UAD 3.6 order but my software isn't verified yet", "Contact us immediately — before starting the report. We can reassign the order or give you additional time to get your software updated. Do not attempt a UAD 3.6 report in unverified software — the output will fail UCDP compliance checks."),
        ("I need more time to complete a UAD 3.6 report", "Contact us as soon as you know — ideally at least 24-48 hours before the due date. We will communicate with the lender on your behalf. Early communication is almost always resolvable. Last-minute communication is much harder to manage."),
        ("I'm not sure if a specific field should be classified as UAD 3.6 or has a question about a new field", "Check Appendix F-1 first — it's the authoritative source. If you still have questions after checking, contact us. We'd rather you ask and get it right than guess and get it wrong."),
        ("I completed a UAD 3.6 report but the lender says they can't accept it", "Contact us immediately. This is a lender system readiness issue, not an appraiser error. We will handle the lender communication and work toward the best resolution available."),
        ("I'm getting revision requests that seem UAD 3.6 specific", "Use the FAQ / Revision Responses tab on this site for pre-written responses to the most common UAD 3.6 revision requests. If you get a revision request that isn't covered there, contact us — we'll help you draft the response and add it to the library."),
        ("I want to start practicing UAD 3.6 but haven't received an order yet", "That's the right approach. Use your software's learning or practice mode and the GSE's sample scenarios (linked in the Training Resources tab) to practice before your first live order. Contact us if you want feedback on a practice report."),
    ]
    for situation, response in situations:
        with st.expander(f"❓ {situation}"):
            st.write(response)

    st.divider()
    st.info("**The bottom line:** UAD 3.6 is a significant change for everyone — appraisers, AMCs, lenders, and software providers. We are all navigating it together. Open communication is the single most important thing you can do to make your transition smooth. We are here, we are reachable, and we want you to succeed.")

    st.divider()
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        if os.path.exists(AVM_LOGO):
            st.image(AVM_LOGO, width=140)
        st.markdown("**Absolute Value Management**")
        st.caption("Your AMC contact for UAD 3.6 questions, order format clarification, and transition support.")
    with col_f2:
        if os.path.exists(ATECH_LOGO):
            st.image(ATECH_LOGO, width=140)
        st.markdown("**A-Tech Appraisal Co.**")
        st.caption("Co-presenter of this resource. Questions about appraisal workflow, software, or field practice.")

# ══════════════════════════════════════════════════════════════════════════════
# ASSIGNMENT INTAKE
# ══════════════════════════════════════════════════════════════════════════════
elif selection == "📄 Assignment Intake":

    st.markdown("Upload your engagement letter and the key assignment details will be extracted and formatted into a clean, copy-pasteable summary card.")
    st.caption("Supported formats: PDF, PNG, JPG. Your document is not stored — it is processed once and discarded.")

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload Engagement Letter",
        type=["pdf", "png", "jpg", "jpeg"],
        help="Upload the engagement letter or order confirmation from your AMC or client."
    )

    st.markdown("#### Or enter details manually")
    st.caption("If you don't have a document to upload, fill in what you have below.")

    with st.expander("✏️ Manual Entry", expanded=not bool(uploaded_file)):
        col_a, col_b = st.columns(2)
        with col_a:
            m_client      = st.text_input("Client / AMC",            key="m_client")
            m_lender      = st.text_input("Lender",                  key="m_lender")
            m_borrower    = st.text_input("Borrower(s)",             key="m_borrower")
            m_address     = st.text_input("Property Address",        key="m_address")
            m_city        = st.text_input("City, State, Zip",        key="m_city")
        with col_b:
            m_effective   = st.text_input("Effective Date",          key="m_effective")
            m_due         = st.text_input("Due Date",                key="m_due")
            m_form        = st.text_input("Form Type",               key="m_form",
                                          placeholder="e.g. URAR UAD 3.6, 1004, 1073")
            m_scope       = st.text_input("Scope / Assignment Type", key="m_scope",
                                          placeholder="e.g. Interior inspection")
            m_intended    = st.text_input("Intended Use",            key="m_intended",
                                          placeholder="e.g. Mortgage financing")
            m_loan        = st.text_input("Loan Type",               key="m_loan",
                                          placeholder="e.g. Conventional, FHA, VA")
            m_fee         = st.text_input("Fee",                     key="m_fee")
            m_file        = st.text_input("File / Order Number",     key="m_file")
        m_notes = st.text_area("Additional Notes / Special Instructions", key="m_notes", height=80)

    st.divider()

    if not ANTHROPIC_AVAILABLE:
        st.warning("⚠️ The `anthropic` package is not installed. Add `anthropic` to your `requirements.txt` to enable document extraction. Manual entry below is fully functional.")

    run_extract = st.button("⚡ Extract Assignment Details", use_container_width=True,
                            disabled=(not uploaded_file or not ANTHROPIC_AVAILABLE),
                            help="Upload a document above to enable extraction.")

    if run_extract and uploaded_file and ANTHROPIC_AVAILABLE:
        with st.spinner("Reading engagement letter..."):
            try:
                file_bytes  = uploaded_file.read()
                b64_data    = base64.standard_b64encode(file_bytes).decode("utf-8")
                suffix      = uploaded_file.name.lower().split(".")[-1]
                if suffix == "pdf":
                    media_type = "application/pdf"
                    doc_block  = {
                        "type": "document",
                        "source": {"type": "base64", "media_type": media_type, "data": b64_data}
                    }
                else:
                    mt_map     = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}
                    media_type = mt_map.get(suffix, "image/jpeg")
                    doc_block  = {
                        "type": "image",
                        "source": {"type": "base64", "media_type": media_type, "data": b64_data}
                    }

                try:
                    api_key = st.secrets["ANTHROPIC_API_KEY"]
                except Exception:
                    api_key = os.environ.get("ANTHROPIC_API_KEY", "")

                client = anthropic.Anthropic(api_key=api_key)

                response = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=1000,
                    messages=[{
                        "role": "user",
                        "content": [
                            doc_block,
                            {
                                "type": "text",
                                "text": """Extract the following fields from this appraisal engagement letter or order confirmation. Return ONLY a valid JSON object with no extra text, preamble, or markdown.

Fields to extract:
{
  "client": "",
  "lender": "",
  "borrower": "",
  "property_address": "",
  "city_state_zip": "",
  "effective_date": "",
  "due_date": "",
  "form_type": "",
  "scope": "",
  "intended_use": "",
  "loan_type": "",
  "fee": "",
  "file_number": "",
  "special_instructions": ""
}

Rules:
- If a field is not found, use an empty string.
- For borrower, include all borrowers listed.
- For form_type, capture exactly as written (e.g. 'URAR UAD 3.6', '1004', '1073').
- For scope, summarize in plain English (e.g. 'Interior inspection — full URAR').
- Do not invent or infer values not present in the document.
- Return only the JSON object."""
                            }
                        ]
                    }]
                )

                raw = response.content[0].text.strip()
                raw = raw.replace("```json", "").replace("```", "").strip()
                extracted = json.loads(raw)
                st.session_state["intake_extracted"] = extracted
                st.success("✅ Extraction complete.")

            except json.JSONDecodeError:
                st.error("Could not parse the extracted data. Try the manual entry fields below.")
                st.session_state["intake_extracted"] = None
            except Exception as e:
                st.error(f"Extraction failed: {e}")
                st.session_state["intake_extracted"] = None

    # ── Build display data from extracted OR manual entry ──────────────────────
    extracted = st.session_state.get("intake_extracted")

    def pick(extracted_val, manual_val):
        """Use extracted if available and non-empty, otherwise fall back to manual."""
        if extracted and extracted.get(extracted_val):
            return extracted[extracted_val]
        return manual_val or ""

    d = {
        "Client / AMC":              pick("client",               st.session_state.get("m_client", "")),
        "Lender":                    pick("lender",               st.session_state.get("m_lender", "")),
        "Borrower(s)":               pick("borrower",             st.session_state.get("m_borrower", "")),
        "Property Address":          pick("property_address",     st.session_state.get("m_address", "")),
        "City, State, Zip":          pick("city_state_zip",       st.session_state.get("m_city", "")),
        "Effective Date":            pick("effective_date",       st.session_state.get("m_effective", "")),
        "Due Date":                  pick("due_date",             st.session_state.get("m_due", "")),
        "Form Type":                 pick("form_type",            st.session_state.get("m_form", "")),
        "Scope / Assignment Type":   pick("scope",                st.session_state.get("m_scope", "")),
        "Intended Use":              pick("intended_use",         st.session_state.get("m_intended", "")),
        "Loan Type":                 pick("loan_type",            st.session_state.get("m_loan", "")),
        "Fee":                       pick("fee",                  st.session_state.get("m_fee", "")),
        "File / Order Number":       pick("file_number",          st.session_state.get("m_file", "")),
        "Special Instructions":      pick("special_instructions", st.session_state.get("m_notes", "")),
    }

    has_any = any(v.strip() for v in d.values())

    if has_any:
        st.divider()
        st.markdown("### 📋 Assignment Summary Card")
        st.caption("Review, edit if needed, then copy to clipboard or paste directly into TOTAL or your workfile.")

        col_card, col_edit = st.columns([3, 1])
        with col_edit:
            edit_mode = st.toggle("✏️ Edit fields", key="edit_mode")

        if edit_mode:
            edited = {}
            for label, val in d.items():
                edited[label] = st.text_input(label, value=val, key=f"edit_{label}")
            d = edited

        # Display card
        st.markdown("---")
        col1, col2 = st.columns(2)
        items = list(d.items())
        mid   = len(items) // 2
        for label, val in items[:mid]:
            with col1:
                st.markdown(f"**{label}**")
                st.write(val if val else "—")
        for label, val in items[mid:]:
            with col2:
                st.markdown(f"**{label}**")
                st.write(val if val else "—")

        st.markdown("---")

        # Plain text copy block
        lines = [f"UAD 3.6 ASSIGNMENT SUMMARY", "=" * 40]
        for label, val in d.items():
            if val.strip():
                lines.append(f"{label}: {val}")
        lines.append("=" * 40)
        plain_text = "\n".join(lines)

        st.text_area("📋 Copy-pasteable text", value=plain_text, height=300, key="summary_text")
        st.caption("Select all → copy → paste into TOTAL notes, workfile, or email.")

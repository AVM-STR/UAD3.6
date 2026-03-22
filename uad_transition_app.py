"""
UAD 2.6 → 3.6 Transition Resource
Presented by Absolute Value Management & A-Tech Appraisal Co.
"""

import os
import streamlit as st

ATECH_LOGO = os.path.join(os.path.dirname(__file__), "atech_logo.png")
AVM_LOGO   = os.path.join(os.path.dirname(__file__), "avm_logo.png")

st.set_page_config(
    page_title="UAD 3.6 Transition Guide",
    page_icon="🏠",
    layout="wide"
)

# ── Header ─────────────────────────────────────────────────────────────────────
col_logo1, col_title, col_logo2 = st.columns([1, 4, 1])
with col_logo1:
    if os.path.exists(AVM_LOGO):
        st.image(AVM_LOGO, width=160)
with col_title:
    st.title("UAD 2.6 → 3.6 Transition Guide")
    st.caption("A resource for appraisers navigating the biggest form change in 15 years — presented by Absolute Value Management & A-Tech Appraisal Co.")
with col_logo2:
    if os.path.exists(ATECH_LOGO):
        st.image(ATECH_LOGO, width=160)

st.divider()

# ── Timeline banner ────────────────────────────────────────────────────────────
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

# ── Navigation tabs ────────────────────────────────────────────────────────────
(tab_overview, tab_field_map, tab_inspection,
 tab_ratings, tab_sketch, tab_checklist,
 tab_faq, tab_tools, tab_resources) = st.tabs([
    "📊 What Changed",
    "🗺️ Field Mapper",
    "🔍 Inspection Guide",
    "🏠 C & Q Ratings",
    "📐 Sketch & ANSI",
    "✅ Inspection Checklist",
    "❓ FAQ / Revision Responses",
    "💻 Software & Tools",
    "📚 Training Resources"
])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — WHAT CHANGED
# ══════════════════════════════════════════════════════════════════════════════
with tab_overview:
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
with tab_field_map:
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
with tab_inspection:
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
with tab_ratings:
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
with tab_sketch:
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
with tab_checklist:
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

# ══════════════════════════════════════════════════════════════════════════════
# TAB 7 — FAQ / REVISION RESPONSES
# ══════════════════════════════════════════════════════════════════════════════
with tab_faq:
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
with tab_tools:
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
        st.link_button("▶ Watch Demo — UAD 3.6 in Minutes (Storyboard EMP)", "https://www.bigmarker.com/communities/Storyboard-EMP/conferences")

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
        st.link_button("▶ Watch Demo — Appraisal Update Podcast (3.3.26)", "https://www.youtube.com/@appraiserelearning")
        st.link_button("▶ Watch Demo — Aivre Walkthrough Webinar", "https://www.bigmarker.com/Storyboard-EMP/live-webinar-transforming-appraisals-with-aivre-the-first-gse-verified-software-for-uad-3-6")

    st.divider()
    st.markdown("### Software demo videos — watch before you decide")
    st.caption("These videos show real workflows in real software — the fastest way to evaluate before committing.")

    demos = [
        ("TOTAL by a la mode", "Live Demo: How to use UAD 3.6 within TOTAL (Storyboard EMP)", "https://blogs.alamode.com/live-demo-with-storyboard-emp-how-to-use-uad-3.6-within-total", "Storyboard EMP hosted this live demo showing the full UAD 3.6 workflow in TOTAL, the most widely used traditional platform. Good starting point if you're a current TOTAL user."),
        ("Aivre", "The Appraisal Update Podcast — UAD 3.6 and AI: How Aivre Is Changing Appraisers' Workflows (3.3.26)", "https://www.youtube.com/@appraiserelearning", "Bryan Reynolds and Aivre CEO Jake Lew walk through the software live, including a screen-share demo. The most current look at Aivre's UAD 3.6 workflow."),
        ("Aivre", "Aivre Appraisal Software Walkthrough Webinar — UAD 3.6, AI & Automation for Appraisers", "https://www.bigmarker.com/Storyboard-EMP/live-webinar-transforming-appraisals-with-aivre-the-first-gse-verified-software-for-uad-3-6", "Full platform walkthrough webinar hosted by Storyboard EMP. Covers data entry, photo classification, analytics, and compliance checking in detail."),
        ("Automax", "Webinar: Copilot to the Future — UAD 3.6 in Minutes by Storyboard EMP", "https://www.bigmarker.com/communities/Storyboard-EMP/conferences", "Automax's UAD 3.6 demo webinar hosted by Storyboard EMP. Shows how Automax handles the full report workflow including sketch generation."),
        ("SFREP / Appraise-It Pro", "Writing a UAD 3.6 Report in Appraise-It Pro", "https://www.sfrep.com/training/videos/", "SFREP walks through the UAD 3.6 dynamic URAR in their Appraise-It Pro software. Notable: SFREP was the first of the 'big four' platforms to obtain GSE verification. Free 6-month trial available."),
        ("ACI", "UAD 3.6 and ACI Solutions — Hosted by NAN", "https://nan-amc.com/uad_3_6/", "Nationwide Appraisal Network hosted this webinar with ACI covering how their platform handles UAD 3.6 compliance, ordering, and delivery."),
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
with tab_resources:
    st.subheader("Training Resources & Reference Materials")
    st.markdown("The best UAD 3.6 resources — curated and organized so you don't have to hunt across multiple sites.")

    st.markdown("### 📋 Start here — free GSE resources")
    gse_resources = [
        ("Appendix F-1: URAR Reference Guide", "fanniemae.com/UAD", "The authoritative field-by-field reference for the new URAR. 375 pages — download the PDF and keep it searchable. If you have a question about a specific field, this is the answer. Worth printing the most-used sections."),
        ("UAD Inspection and Reporting Tips", "fanniemae.com/UAD", "Published Oct 2025 by Fannie Mae and Freddie Mac. A concise job aid highlighting notable differences in information collected between UAD 2.6 and 3.6. Best quick-reference document for inspection prep."),
        ("Sample URAR Scenarios (Appendix D)", "fanniemae.com/UAD", "Example completed reports showing what a UAD 3.6 URAR actually looks like for different property types. Essential for understanding what completed reports should contain."),
        ("Fannie Mae UAD 3.6 Training Videos", "fanniemae.com/UAD", "Free video series from Fannie Mae covering the new URAR structure, dynamic form behavior, and key field requirements. Best starting point before attempting a 3.6 report."),
        ("Freddie Mac UAD Resources", "sf.freddiemac.com/tools-learning/uniform-mortgage-data-program/uad", "Freddie Mac's equivalent resource hub — includes their policy bulletin (2025-7) and supplemental guidance. Some nuances differ from Fannie Mae policy."),
        ("UAD 3.6 FAQ", "fanniemae.com/UAD", "Official FAQ from Fannie Mae and Freddie Mac answering the most common implementation questions. Updated periodically as new questions emerge."),
        ("FCC Broadband Map", "broadbandmap.fcc.gov", "Required for verifying broadband availability at the subject property — new required field in UAD 3.6. Enter the subject address to get the official broadband availability data."),
    ]
    for title, source, desc in gse_resources:
        with st.expander(f"📄 {title}"):
            st.write(desc)
            st.caption(f"Source: {source}")

    st.divider()
    st.markdown("### 🎓 Education and training courses")
    courses = [
        ("Appraiser's Guide to the New URAR (7 hours)", "McKissock Learning", "Comprehensive CE course on the redesigned URAR. 7 hours of CE credit. Covers all major changes, new fields, and reporting requirements. One of the most thorough available."),
        ("UAD 3.6 Bootcamp (in-person)", "Appraiser eLearning", "Intensive multi-day in-person training with hands-on software demos and Q&A with Fannie Mae and Freddie Mac representatives. Joel Baker from a la mode leads mobile appraising sessions. Watch for future dates."),
        ("TOTAL for Mobile UAD 3.6 Training", "a la mode / CoreLogic", "Software-specific training for TOTAL users making the transition to UAD 3.6 and mobile data collection. Available through a la mode's training portal."),
        ("ANSI Z765-2021 Measurement Standard", "ANSI / various providers", "The measurement standard now formalized in UAD 3.6. CE courses covering ANSI are available from McKissock, McKissock, and state appraisal organizations. Essential for understanding GLA, NSFA, and the 7-foot rule."),
    ]
    for title, provider, desc in courses:
        with st.expander(f"🎓 {title}"):
            st.write(desc)
            st.caption(f"Provider: {provider}")

    st.divider()
    st.markdown("### 📰 Recommended reading")
    reading = [
        ("Flooded With Change: Appraisers Tackle a Dynamic URAR and UAD 3.6", "Working RE (Oct 2025)", "workingre.com", "One of the best long-form articles on the practical impact of UAD 3.6 for practicing appraisers. Includes industry leader perspectives and what to watch."),
        ("UAD 3.6 Key Changes (And Resources You Need to Know)", "Appraiser eLearning (Feb 2026)", "appraiserelearning.com", "Bryan Knowlton's practical breakdown of the changes that matter most. Includes the ceiling height requirement, comp drive-by retirement, and broadband field."),
        ("Understanding Appraisal Condition Ratings Under UAD 3.6", "McKissock Learning", "mckissock.com", "Clear breakdown of how the new multi-level C rating structure works and how to apply it correctly."),
        ("The New UAD Quality Equation: Interior + Exterior = Overall Rating", "Working RE (Aug 2025)", "workingre.com", "Specific to the new Q rating reconciliation process — how to assess interior and exterior separately and reconcile to overall."),
        ("UAD 3.6 & ANSI Z765: A Guide to New Appraisal Measurement", "Swish Appraisal", "swishappraisal.com", "Technical but thorough guide to how ANSI Z765-2021 is enforced in UAD 3.6, including the per-floor GLA breakdown requirement and NSFA."),
    ]
    for title, source, url, desc in reading:
        with st.expander(f"📰 {title}"):
            st.write(desc)
            st.caption(f"Source: {source} | {url}")

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

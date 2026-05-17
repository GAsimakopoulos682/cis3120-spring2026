"""
Seeded data for Mini-Project MP03 — Press Release to Plot: Industry Comparison.

These lists are starting points provided by the instructor. Teams are expected
to modify both the ticker lists and the phrase lists during the project.
Modifications must be justified in the methodology section.

The seeds were chosen to give each industry a working starting point, not to
be optimal. The Financial Services seed is biased toward retail-banking events
and undercounts capital-markets activity; the Travel and Hospitality seed
mixes hotel-style and airline-style location events that may warrant separate
treatment in your map. Identifying these limitations and proposing fixes is
the methodology section's purpose.

Reference: docs/MP03_Assignment.docx, Section 3.
"""

# ──────────────────────────────────────────────────────────────────────────
#  Financial Services (default seed: 14 companies across sub-segments)
# ──────────────────────────────────────────────────────────────────────────

FINANCIAL_SERVICES_TICKERS = [
    # Money-center banks
    "JPM", "BAC", "WFC", "C",
    # Regional banks
    "PNC", "USB", "TFC",
    # Asset management
    "BLK", "BX",
    # Insurance
    "MET", "PRU",
    # Payments
    "V", "MA", "AXP",
]

FINANCIAL_SERVICES_PHRASES = [
    '"new branch"',
    '"branch opening"',
    '"branch closure"',
    '"branch closing"',
    '"branch consolidation"',
    '"regional office"',
    '"office closure"',
    '"operations center"',
    '"data center"',
    '"new location"',

    '"branch relocation"',
    '"relocated branch"',
    '"relocation of services"',
    '"service center"',
    '"customer service center"',
    '"contact center"',
    '"call center expansion"',
    '"call center closure"',
    '"operational hub"',
    '"corporate headquarters"',
    '"headquarters relocation"',
    '"administrative office"',
    '"satellite office"',
    '"field office"',
    '"facility expansion"',
    '"facility upgrade"',
    '"facility investment"',
    '"office expansion"',
    '"office move"',
    '"leased space"',
    '"new facility"',
    '"property acquisition"',
    '"real estate transaction"',
    '"real estate sale"',
    '"site redevelopment"',
    '"infrastructure investment"',
    '"operations expansion"',
    '"business expansion"',
    '"strategic footprint"',
    '"market expansion"',
]

# ──────────────────────────────────────────────────────────────────────────
#  Travel and Hospitality (default seed: 14 companies across sub-segments)
# ──────────────────────────────────────────────────────────────────────────

TRAVEL_HOSPITALITY_TICKERS = [
    # Hotels
    "MAR", "HLT", "H", "CHH", "WH",
    # Cruise
    "CCL", "RCL", "NCLH",
    # Airlines
    "DAL", "UAL", "AAL", "LUV",
    # Online travel
    "BKNG", "EXPE",
]

TRAVEL_HOSPITALITY_PHRASES = [
    '"new property"',
    '"new hotel"',
    '"hotel opening"',
    '"resort opening"',
    '"property opening"',
    '"brand conversion"',
    '"new route"',
    '"new gateway"',
    '"new terminal"',
    '"grand opening"',
    
    '"new resort"',
    '"hotel development"',
    '"hospitality development"',
    '"property expansion"',
    '"new hospitality project"',
    '"management agreement"',
    '"franchise agreement"',
    '"new destination"',
    '"new airline route"',
    '"route expansion"',
    '"expanded service"',
    '"new service to"',
    '"international service"',
    '"airport expansion"',
    '"new flight route"',
    '"property acquisition"',
    '"hotel acquisition"',
    '"resort acquisition"',
    '"casino opening"',
    '"new market"',
    '"new location"',
    '"site selection"',
    '"facility opening"',
    '"new facility"',
    '"expansion project"',
    '"construction project"',
    '"opening ceremony"',
    '"development project"',
    '"real estate development"',
    '"mixed-use development"',
]

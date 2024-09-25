# branch tags
army_tags = [r"army", r"usarmy", r"soldier", r"bde", r" u s a", r"usa",
             r"soidier", r"us arm", r"solder"]
air_force_tags = [r"air force", r"usaf", r"airforce", r"u s a f", r"afb", r"a f b",
             r"a f", r"\baf\b", r"air guard", r"ujaf"]
navy_tags = [r"navy", r"naval", r"usn", r"seamen", r"sailor", r"usnavy", r"usn",
            r"u s n", r"c6f det", r"nscwcdd", r"us nave", r"seal", r"nswc",]
reserves_tags = [r"reserve", r"usar", r"usafr", r"national guard",
                 r"natl guard", r"nationalguard", r"ng",
                 r"national g", r"state", r"air national", r"dmna", r"nat guard",
                 r"air guard", r"air national guard", r"a n g", r"natuonal guard",
                 r"nat, guard"]
marines_tags = [r"marines", r"marine corps", r"usmc", r"marine corp",
                r"marine", r"amrine corp"]
cg_mm_tags = [r"coast guard", r"uscg", r"coastal guard", r"coastguard",
                    r"merchant marine", r"coast guart", r"coast gurard"]
civilian_tags = [r"government worker", r"librarian", r"contractor", r"KBR",
                 r"L3", r" inc", r"natural gas", r"& sons", r"saic",
                 r"clocks by hollis",
                 r"morgan", r"high s", r"consultant", r"employee", r"club",
                 r"homemaker", r"social worker", r"therapist", r"manager",
                 r"px worker", r"teacher", r"historian", r"holland & knight",
                 r"mpri", r"conress", r"congress", r"citizen", r"consular",
                 r"consultant", r"coldwell", r"waccamaw", r"bank", r"civil servant",
                 r"self employed", r"coastal conservation league", r"taxpayer",
                 r"ceg corp", r"usdol", r"fashion magic", r"senate", r"comtek",
                 r"concerned americans", r"volunteer", r"senator", r"spouse",
                 r"usg", r"govt worker", r"gov worker", r"government worker",
                 r"public servant", r"self-employed", r"law enforcement", r"gvt",
                 r"ssa", r"nasa", r"federal worker", r"republican", r"democrat",
                 r"city planner", r"envir protection agency", r"\bepa\b", r"agstat",
                 r"patriot", r"ambassador to ireland", r"photographer", r"auto country",
                 r"ninja", r"federal meat inspector", r"diplomat", r"house of representatives",
                 r"usphs", r"usa jax", r"custom oficer", r"us forest service",
                 r"operation earth regeneration", r"yes", r"government services",
                 r"homeland security", r"driver", r"civil service", r"government policy",
                 r"us representative", r"dance", r"president", r"c i a", r"dignity"]
officer_tags = [r"officer", r"captain", r"lieutenant", r"lt", r"lt", r"ltcol",
                r"ist", r"adml", r"rdml", r"vadm", r"colonel",
                r"veterinarian", r"chaplain", r"attorney", r"nurse",
                r"captain", r"major", r"pilot", r"surgeon", r"ologist",
                r"judge", r"lawyer", r"col", r"fa", r"social security",
                r"us customs", r"logistic"]
former_military_tags = [r"veteran", r"vet", r"disabled"]


# boolean tags
retired_tags = [r"retire", r"retired", r"ret", r"reired", r"dmna", r"retiree",
                r"retiered"]

# ignored tags
not_officer_tags = ["security officer", r"human resources"]
not_former_military_tags = [r"veterinarian"]

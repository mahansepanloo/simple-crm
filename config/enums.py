GenderEnum = [
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
]

AGENT_TYPE_CHOICES = [
    ("A", "agent"),
    ("B", "branch")
]

STATUS_CHOICES = [
    (0, "close"),
    (1, "open"),
    (-1, "pending"),
]


STATUS_CHOICES_ACCOUNT = [
    (0, "active"),
    (1, "deactivate"),
]



STATUS_TRANSACTION = [
    (0, "pending"),
    (1, "approved"),
    (2, "canceled"),
] 


STATUS_TYPE = [
    ('charge', 'charge'),
    ('decharge', 'decharge'),
]


JOB_TYPE = [
    (0, "seven"),
    (1, "gspn")
]

SWAP_OR_REFUND = [
    (0, "swap"),
    (1, "refund")
]
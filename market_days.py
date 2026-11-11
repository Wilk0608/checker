"""NYSE calendar for the plan year: full-day holidays and early closes (1:00 PM New York time).
Standard library only, so the workflow's gate can import it before any package is installed."""
import datetime as dt

HOLIDAYS = {dt.date(2026, 11, 26), dt.date(2026, 12, 25), dt.date(2027, 1, 1), dt.date(2027, 1, 18), dt.date(2027, 2, 15),
            dt.date(2027, 3, 26), dt.date(2027, 5, 31), dt.date(2027, 6, 18), dt.date(2027, 7, 5), dt.date(2027, 9, 6)}
EARLY_CLOSES = {dt.date(2026, 11, 27), dt.date(2026, 12, 24)}

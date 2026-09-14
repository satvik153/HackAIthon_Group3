"""
============================================================
TERRALOOP 🌍
Measure Waste. Close the Loop.

Smart Household Waste & Recycling Manager
Myra's Global Tech HACK-AI-THON 2026

OOP + Python Fundamentals + SDGs

Main Features
-------------
• Household and WasteRecord classes
• Add / Update / Delete / Search records
• Waste statistics and category analysis
• Recycling rate
• Sustainability score
• Rule-based recommendations
• Waste hotspot detection
• What-If sustainability simulator
• Selected-period reports
• Report export to TXT
• SDG 11, SDG 12 and SDG 13 alignment

Install:
    py -3.14 -m pip install Pillow

Run:
    F5 in IDLE
============================================================
"""

import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from PIL import Image, ImageTk, ImageDraw
from datetime import date, datetime, timedelta


# ============================================================
# COLOURS
# ============================================================

BG = "#F7F8FC"
MINT = "#D8F3E5"
MINT2 = "#B8E6D0"
BLUE = "#DDEBFA"
PINK = "#F9DDE8"
LILAC = "#E8DDF8"
YELLOW = "#FFF0C7"
WHITE = "#FFFFFF"
GREEN = "#3C9675"
DARK = "#294052"
GREY = "#718096"
RED = "#D96C6C"
ORANGE = "#E8A44A"


CATEGORIES = [
    "Plastic",
    "Paper",
    "Organic",
    "Glass",
    "Metal",
    "E-Waste"
]


# ============================================================
# OOP MODEL 1 — HOUSEHOLD
# ============================================================

class Household:

    def __init__(self, name="My Household", members=4):
        self.name = name
        self.members = members

    def description(self):
        return f"{self.name} • {self.members} members"


# ============================================================
# OOP MODEL 2 — WASTE RECORD
# ============================================================

class WasteRecord:

    def __init__(
        self,
        record_id,
        record_date,
        category,
        weight,
        recycled,
        note=""
    ):
        self.record_id = record_id
        self.record_date = record_date
        self.category = category
        self.weight = float(weight)
        self.recycled = bool(recycled)
        self.note = note

    def status(self):
        if self.recycled:
            return "♻ Recycled"
        return "Not Recycled"


# ============================================================
# OOP CLASS 3 — WASTE MANAGER
# ============================================================

class WasteManager:

    def __init__(self, load_sample_data=True):

        self.records = []
        self.next_id = 1

        if load_sample_data:
            self.load_sample_data()

    # --------------------------------------------------------
    # SAMPLE DATA
    # --------------------------------------------------------

    def load_sample_data(self):

        sample_records = [
            (
                "2026-09-01",
                "Plastic",
                1.8,
                True,
                "Bottles and packaging"
            ),
            (
                "2026-09-03",
                "Organic",
                3.2,
                True,
                "Kitchen waste"
            ),
            (
                "2026-09-05",
                "Paper",
                1.4,
                True,
                "Newspapers"
            ),
            (
                "2026-09-07",
                "Glass",
                1.1,
                True,
                "Glass jars"
            ),
            (
                "2026-09-09",
                "E-Waste",
                0.7,
                False,
                "Old cables"
            ),
            (
                "2026-09-11",
                "Plastic",
                2.1,
                False,
                "Mixed plastic"
            )
        ]

        for record in sample_records:
            self.add_record(*record)

    # --------------------------------------------------------
    # ADD
    # --------------------------------------------------------

    def add_record(
        self,
        record_date,
        category,
        weight,
        recycled,
        note=""
    ):

        record = WasteRecord(
            self.next_id,
            record_date,
            category,
            weight,
            recycled,
            note
        )

        self.records.append(record)
        self.next_id += 1

        return record

    # --------------------------------------------------------
    # UPDATE
    # --------------------------------------------------------

    def update_record(
        self,
        record_id,
        record_date,
        category,
        weight,
        recycled,
        note
    ):

        for record in self.records:

            if record.record_id == record_id:

                record.record_date = record_date
                record.category = category
                record.weight = float(weight)
                record.recycled = bool(recycled)
                record.note = note

                return True

        return False

    # --------------------------------------------------------
    # DELETE
    # --------------------------------------------------------

    def delete_record(self, record_id):

        for record in self.records:

            if record.record_id == record_id:

                self.records.remove(record)

                return True

        return False

    # --------------------------------------------------------
    # SEARCH
    # --------------------------------------------------------

    def search(self, text="", category="All"):

        text = text.lower().strip()

        results = []

        for record in self.records:

            category_match = (
                category == "All"
                or record.category == category
            )

            text_match = (
                not text
                or text in record.category.lower()
                or text in record.note.lower()
                or text in record.record_date.lower()
            )

            if category_match and text_match:
                results.append(record)

        return sorted(
            results,
            key=lambda x: x.record_date,
            reverse=True
        )

    # --------------------------------------------------------
    # DATE FILTER
    # --------------------------------------------------------

    def filter_period(self, period):

        if period == "All Time":
            return list(self.records)

        today = date.today()

        if period == "Last 7 Days":
            start_date = today - timedelta(days=6)

        elif period == "Last 30 Days":
            start_date = today - timedelta(days=29)

        else:
            return list(self.records)

        filtered = []

        for record in self.records:

            try:
                record_date = datetime.strptime(
                    record.record_date,
                    "%Y-%m-%d"
                ).date()

                if start_date <= record_date <= today:
                    filtered.append(record)

            except ValueError:
                continue

        return filtered


# ============================================================
# OOP CLASS 4 — WASTE ANALYZER
# ============================================================

class WasteAnalyzer:

    def __init__(self, records):
        self.records = records

    # --------------------------------------------------------
    # TOTAL WASTE
    # --------------------------------------------------------

    def total_waste(self):

        return sum(
            record.weight
            for record in self.records
        )

    # --------------------------------------------------------
    # RECYCLED WASTE
    # --------------------------------------------------------

    def recycled_waste(self):

        return sum(
            record.weight
            for record in self.records
            if record.recycled
        )

    # --------------------------------------------------------
    # RECYCLING RATE
    # --------------------------------------------------------

    def recycling_rate(self):

        total = self.total_waste()

        if total == 0:
            return 0

        return (
            self.recycled_waste() / total
        ) * 100

    # --------------------------------------------------------
    # CATEGORY BREAKDOWN
    # --------------------------------------------------------

    def category_breakdown(self):

        data = {}

        for category in CATEGORIES:

            amount = sum(
                record.weight
                for record in self.records
                if record.category == category
            )

            if amount > 0:
                data[category] = amount

        return data

    # --------------------------------------------------------
    # CATEGORY PERCENTAGES
    # --------------------------------------------------------

    def category_percentages(self):

        total = self.total_waste()

        if total == 0:
            return {}

        return {
            category: (weight / total) * 100
            for category, weight
            in self.category_breakdown().items()
        }

    # --------------------------------------------------------
    # HOTSPOT
    # --------------------------------------------------------

    def hotspot(self):

        breakdown = self.category_breakdown()

        if not breakdown:
            return None, 0

        category = max(
            breakdown,
            key=breakdown.get
        )

        total = self.total_waste()

        percentage = (
            breakdown[category] / total * 100
            if total
            else 0
        )

        return category, percentage

    # --------------------------------------------------------
    # E-WASTE PERCENTAGE
    # --------------------------------------------------------

    def e_waste_percentage(self):

        total = self.total_waste()

        if total == 0:
            return 0

        e_waste = sum(
            record.weight
            for record in self.records
            if record.category == "E-Waste"
        )

        return (e_waste / total) * 100

    # --------------------------------------------------------
    # SUSTAINABILITY SCORE
    # --------------------------------------------------------

    def sustainability_score(self):

        if not self.records:
            return 0

        total = self.total_waste()

        if total == 0:
            return 0

        recycling = self.recycling_rate()

        # ----------------------------------------------------
        # Component 1: Recycling
        # Maximum = 60 points
        # ----------------------------------------------------

        recycling_points = (
            recycling * 0.60
        )

        # ----------------------------------------------------
        # Component 2: Waste Diversification
        #
        # A household whose waste is extremely concentrated
        # in one category has more opportunity to improve.
        #
        # Maximum = 20 points
        # ----------------------------------------------------

        percentages = self.category_percentages()

        if percentages:

            largest_percentage = max(
                percentages.values()
            )

            diversification_points = max(
                0,
                20 - (largest_percentage * 0.20)
            )

        else:
            diversification_points = 0

        # ----------------------------------------------------
        # Component 3: E-Waste Responsibility
        #
        # Maximum = 20 points.
        # Lower e-waste share = better score.
        # ----------------------------------------------------

        e_waste_percentage = (
            self.e_waste_percentage()
        )

        e_waste_points = max(
            0,
            20 - e_waste_percentage
        )

        score = (
            recycling_points
            + diversification_points
            + e_waste_points
        )

        return round(
            min(100, max(0, score))
        )

    # --------------------------------------------------------
    # GRADE
    # --------------------------------------------------------

    def grade(self):

        score = self.sustainability_score()

        if score >= 90:
            return "Outstanding 🌟"

        if score >= 75:
            return "Excellent 🌿"

        if score >= 60:
            return "Good 👍"

        if score >= 40:
            return "Improving 🌱"

        return "Needs Attention 💚"


# ============================================================
# OOP CLASS 5 — RECOMMENDATION ENGINE
# ============================================================

class RecommendationEngine:

    ACTIONS = {

        "Plastic":
            "Reduce single-use plastic. Use reusable bottles, "
            "bags and refillable containers.",

        "Paper":
            "Reuse one-sided paper and prefer digital documents "
            "when practical.",

        "Organic":
            "Separate kitchen waste and compost suitable "
            "organic material.",

        "Glass":
            "Reuse jars and bottles and keep clean glass "
            "separate for recycling.",

        "Metal":
            "Collect metal cans separately and reuse durable "
            "metal containers where possible.",

        "E-Waste":
            "Keep electronic waste separate and send it to "
            "an authorized e-waste collection facility."
    }

    def __init__(self, analyzer):
        self.analyzer = analyzer

    def generate(self):

        recommendations = []

        percentages = (
            self.analyzer.category_percentages()
        )

        # ----------------------------------------------------
        # Category-based recommendations
        # ----------------------------------------------------

        for category, percentage in percentages.items():

            if percentage >= 25:

                recommendations.append(
                    (
                        category,
                        f"High hotspot: {percentage:.1f}% of "
                        f"your waste. "
                        + self.ACTIONS.get(
                            category,
                            "Try to reduce this waste category."
                        )
                    )
                )

        # ----------------------------------------------------
        # Recycling recommendation
        # ----------------------------------------------------

        recycling_rate = (
            self.analyzer.recycling_rate()
        )

        if recycling_rate < 50:

            recommendations.append(
                (
                    "Recycling",
                    f"Your recycling rate is only "
                    f"{recycling_rate:.1f}%. Improve segregation "
                    "and send recyclable material to proper "
                    "collection channels."
                )
            )

        elif recycling_rate >= 75:

            recommendations.append(
                (
                    "Recycling",
                    f"Excellent recycling rate of "
                    f"{recycling_rate:.1f}%. Keep maintaining "
                    "good segregation habits."
                )
            )

        # ----------------------------------------------------
        # E-waste recommendation
        # ----------------------------------------------------

        e_waste_percentage = (
            self.analyzer.e_waste_percentage()
        )

        if e_waste_percentage > 10:

            recommendations.append(
                (
                    "E-Waste Alert",
                    f"E-waste represents "
                    f"{e_waste_percentage:.1f}% of your "
                    "recorded waste. Store it separately and "
                    "use authorized disposal channels."
                )
            )

        # ----------------------------------------------------
        # Final fallback
        # ----------------------------------------------------

        if not recommendations:

            recommendations.append(
                (
                    "Great Work! 🌱",
                    "Your waste profile is currently balanced. "
                    "Keep reducing, reusing, segregating and "
                    "recycling responsibly."
                )
            )

        return recommendations


# ============================================================
# OOP CLASS 6 — WHAT-IF SIMULATOR
# ============================================================

class SustainabilitySimulator:

    def __init__(self, records):
        self.records = records

    def simulate_reduction(
        self,
        category,
        reduction_percentage
    ):

        reduction = (
            reduction_percentage / 100
        )

        simulated = []

        for record in self.records:

            new_weight = record.weight

            if record.category == category:

                new_weight = (
                    record.weight
                    * (1 - reduction)
                )

            simulated.append(
                WasteRecord(
                    record.record_id,
                    record.record_date,
                    record.category,
                    new_weight,
                    record.recycled,
                    record.note
                )
            )

        current = WasteAnalyzer(
            self.records
        )

        future = WasteAnalyzer(
            simulated
        )

        return current, future


# ============================================================
# OOP CLASS 7 — TERRALOOP APPLICATION
# ============================================================

class TerraLoopApp(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title(
            "TerraLoop • Smart Waste & Recycling Manager"
        )

        self.geometry("1100x720")
        self.minsize(950, 650)

        self.configure(bg=BG)

        self.household = Household()

        self.manager = WasteManager()

        self.pic = self.make_ecopic()

        self.build()

        self.dashboard()

    # ========================================================
    # IMAGE
    # ========================================================

    def make_ecopic(self):

        img = Image.new(
            "RGB",
            (180, 150),
            "#DFF4E9"
        )

        d = ImageDraw.Draw(img)

        # Tree trunk
        d.rectangle(
            (85, 88, 97, 125),
            fill="#B77B55"
        )

        # Tree
        d.ellipse(
            (48, 35, 105, 100),
            fill="#8ED6A8"
        )

        d.ellipse(
            (82, 25, 140, 95),
            fill="#A9E3BA"
        )

        # Recycling bin
        d.rounded_rectangle(
            (10, 65, 60, 125),
            10,
            fill="#9DD6F0",
            outline="#4E91B7",
            width=3
        )

        d.rectangle(
            (18, 57, 52, 68),
            fill="#4E91B7"
        )

        # Face
        d.ellipse(
            (24, 88, 29, 93),
            fill=DARK
        )

        d.ellipse(
            (42, 88, 47, 93),
            fill=DARK
        )

        d.arc(
            (28, 88, 44, 105),
            0,
            180,
            fill=DARK,
            width=2
        )

        return ImageTk.PhotoImage(img)

    # ========================================================
    # BUILD GUI
    # ========================================================

    def build(self):

        # ----------------------------------------------------
        # SIDEBAR
        # ----------------------------------------------------

        side = tk.Frame(
            self,
            bg=MINT,
            width=220
        )

        side.pack(
            side="left",
            fill="y"
        )

        side.pack_propagate(False)

        tk.Label(
            side,
            text="♻ TerraLoop",
            font=("Arial", 24, "bold"),
            bg=MINT,
            fg=GREEN
        ).pack(pady=(30, 3))

        tk.Label(
            side,
            text="MEASURE • WASTE • CLOSE THE LOOP",
            font=("Arial", 8, "bold"),
            bg=MINT,
            fg=GREY
        ).pack(pady=(0, 25))

        buttons = [

            ("⌂   Dashboard",
             self.dashboard),

            ("＋   Add Waste",
             self.add_window),

            ("▣   Records",
             self.records_window),

            ("🔎  Hotspot & Analysis",
             self.analysis_window),

            ("🌱  Recommendations",
             self.recommendations_window),

            ("🔮  What-If Simulator",
             self.simulator_window),

            ("📄  Report",
             self.report_window)
        ]

        for text, command in buttons:

            tk.Button(
                side,
                text=text,
                command=command,
                font=("Arial", 11, "bold"),
                anchor="w",
                bd=0,
                padx=15,
                pady=10,
                bg=MINT,
                activebackground=MINT2,
                fg=DARK,
                cursor="hand2"
            ).pack(
                fill="x",
                padx=10,
                pady=2
            )

        tk.Frame(
            side,
            bg=MINT
        ).pack(
            expand=True,
            fill="both"
        )

        tk.Label(
            side,
            text="SDG IMPACT",
            font=("Arial", 11, "bold"),
            bg=MINT,
            fg=GREEN
        ).pack()

        tk.Label(
            side,
            text="11  Sustainable Cities\n"
                 "12  Responsible Consumption\n"
                 "13  Climate Action",
            justify="left",
            font=("Arial", 9),
            bg=MINT,
            fg=DARK
        ).pack(pady=15)

        # ----------------------------------------------------
        # MAIN AREA
        # ----------------------------------------------------

        self.main = tk.Frame(
            self,
            bg=BG
        )

        self.main.pack(
            side="right",
            fill="both",
            expand=True
        )

    # ========================================================
    # HELPERS
    # ========================================================

    def clear(self):

        for widget in self.main.winfo_children():
            widget.destroy()

    def card(self, parent, colour=WHITE):

        return tk.Frame(
            parent,
            bg=colour,
            highlightbackground="#E5E8EF",
            highlightthickness=1
        )

    def create_title(self, text, sub=""):

        tk.Label(
            self.main,
            text=text,
            font=("Arial", 25, "bold"),
            bg=BG,
            fg=DARK
        ).pack(
            anchor="w",
            padx=30,
            pady=(25, 2)
        )

        if sub:

            tk.Label(
                self.main,
                text=sub,
                font=("Arial", 10),
                bg=BG,
                fg=GREY
            ).pack(
                anchor="w",
                padx=30
            )

    def get_records_for_period(self, period):

        return self.manager.filter_period(period)

    # ========================================================
    # DASHBOARD
    # ========================================================

    def dashboard(self):

        self.clear()

        self.create_title(
            "Good day, Eco Champion 🌿",
            "Measure waste • Understand patterns • Close the loop"
        )

        # ----------------------------------------------------
        # Period selector
        # ----------------------------------------------------

        filter_bar = tk.Frame(
            self.main,
            bg=BG
        )

        filter_bar.pack(
            fill="x",
            padx=30,
            pady=(15, 0)
        )

        tk.Label(
            filter_bar,
            text="View period:",
            font=("Arial", 10, "bold"),
            bg=BG,
            fg=DARK
        ).pack(side="left")

        period = ttk.Combobox(
            filter_bar,
            values=[
                "Last 7 Days",
                "Last 30 Days",
                "All Time"
            ],
            state="readonly",
            width=15
        )

        period.set("All Time")

        period.pack(
            side="left",
            padx=10
        )

        def refresh_dashboard():

            selected = period.get()

            self.clear()

            self.create_title(
                "Good day, Eco Champion 🌿",
                f"Viewing: {selected} • "
                "Measure waste • Understand patterns • Close the loop"
            )

            self.build_dashboard_content(
                selected
            )

        period.bind(
            "<<ComboboxSelected>>",
            lambda event: refresh_dashboard()
        )

        self.build_dashboard_content(
            "All Time"
        )

    # ========================================================
    # DASHBOARD CONTENT
    # ========================================================

    def build_dashboard_content(self, period):

        records = self.get_records_for_period(
            period
        )

        analyzer = WasteAnalyzer(records)

        total = analyzer.total_waste()
        rate = analyzer.recycling_rate()
        score = analyzer.sustainability_score()

        # ----------------------------------------------------
        # Hero
        # ----------------------------------------------------

        hero = self.card(
            self.main,
            PINK
        )

        hero.pack(
            fill="x",
            padx=30,
            pady=15
        )

        left = tk.Frame(
            hero,
            bg=PINK
        )

        left.pack(
            side="left",
            padx=25,
            pady=18
        )

        tk.Label(
            left,
            text="Measure Waste. Close the Loop. ♻",
            font=("Arial", 19, "bold"),
            bg=PINK,
            fg=DARK
        ).pack(anchor="w")

        tk.Label(
            left,
            text="TerraLoop turns household waste data\n"
                 "into practical sustainability decisions.",
            font=("Arial", 10),
            bg=PINK,
            fg=GREY
        ).pack(
            anchor="w",
            pady=8
        )

        tk.Button(
            left,
            text="＋ Record Waste",
            command=self.add_window,
            bg=GREEN,
            fg=WHITE,
            bd=0,
            font=("Arial", 10, "bold"),
            padx=18,
            pady=8,
            cursor="hand2"
        ).pack(anchor="w")

        tk.Label(
            hero,
            image=self.pic,
            bg=PINK
        ).pack(
            side="right",
            padx=25,
            pady=5
        )

        # ----------------------------------------------------
        # Statistics
        # ----------------------------------------------------

        stats = tk.Frame(
            self.main,
            bg=BG
        )

        stats.pack(
            fill="x",
            padx=30
        )

        self.stat(
            stats,
            "♻",
            "TOTAL WASTE",
            f"{total:.1f} kg",
            MINT
        )

        self.stat(
            stats,
            "♻",
            "RECYCLING RATE",
            f"{rate:.0f}%",
            BLUE
        )

        self.stat(
            stats,
            "★",
            "SUSTAINABILITY",
            f"{score}/100",
            LILAC
        )

        self.stat(
            stats,
            "📋",
            "RECORDS",
            str(len(records)),
            YELLOW
        )

        # ----------------------------------------------------
        # Hotspot
        # ----------------------------------------------------

        category, percentage = analyzer.hotspot()

        hotspot_text = (
            f"{category} • {percentage:.0f}%"
            if category
            else "No data"
        )

        hotspot_card = self.card(
            self.main,
            YELLOW
        )

        hotspot_card.pack(
            fill="x",
            padx=30,
            pady=15
        )

        tk.Label(
            hotspot_card,
            text="🔎 Current Waste Hotspot",
            font=("Arial", 14, "bold"),
            bg=YELLOW,
            fg=DARK
        ).pack(
            side="left",
            padx=18,
            pady=12
        )

        tk.Label(
            hotspot_card,
            text=hotspot_text,
            font=("Arial", 14, "bold"),
            bg=YELLOW,
            fg=GREEN
        ).pack(
            side="left"
        )

        # ----------------------------------------------------
        # Bottom Cards
        # ----------------------------------------------------

        bottom = tk.Frame(
            self.main,
            bg=BG
        )

        bottom.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=5
        )

        # Mission card
        info = self.card(
            bottom,
            WHITE
        )

        info.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 8)
        )

        tk.Label(
            info,
            text="🌱 TerraLoop Mission",
            font=("Arial", 17, "bold"),
            bg=WHITE,
            fg=DARK
        ).pack(
            anchor="w",
            padx=18,
            pady=15
        )

        tk.Label(
            info,
            text="Record → Analyze → Act → Simulate → Improve",
            font=("Arial", 12, "bold"),
            bg=WHITE,
            fg=GREEN
        ).pack(
            anchor="w",
            padx=18
        )

        tk.Label(
            info,
            text="\nTerraLoop supports:\n\n"
                 "• SDG 11 — Sustainable Cities\n"
                 "• SDG 12 — Responsible Consumption\n"
                 "• SDG 13 — Climate Action\n\n"
                 "The goal is not simply to measure waste,\n"
                 "but to turn measurements into action.",
            font=("Arial", 10),
            bg=WHITE,
            fg=GREY,
            justify="left"
        ).pack(
            anchor="w",
            padx=18
        )

        # Score card
        score_card = self.card(
            bottom,
            MINT
        )

        score_card.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(8, 0)
        )

        tk.Label(
            score_card,
            text="🌿 Sustainability Status",
            font=("Arial", 17, "bold"),
            bg=MINT,
            fg=DARK
        ).pack(
            anchor="w",
            padx=18,
            pady=15
        )

        tk.Label(
            score_card,
            text=f"{score}/100",
            font=("Arial", 30, "bold"),
            bg=MINT,
            fg=GREEN
        ).pack(
            anchor="w",
            padx=18
        )

        tk.Label(
            score_card,
            text=analyzer.grade(),
            font=("Arial", 12, "bold"),
            bg=MINT,
            fg=DARK
        ).pack(
            anchor="w",
            padx=18,
            pady=5
        )

        tk.Label(
            score_card,
            text="Based on recycling, waste distribution\n"
                 "and responsible e-waste handling.",
            font=("Arial", 10),
            bg=MINT,
            fg=GREY,
            justify="left"
        ).pack(
            anchor="w",
            padx=18
        )

    # ========================================================
    # STAT CARD
    # ========================================================

    def stat(
        self,
        parent,
        icon,
        heading,
        value,
        colour
    ):

        box = self.card(
            parent,
            colour
        )

        box.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )

        tk.Label(
            box,
            text=icon,
            font=("Arial", 20),
            bg=colour,
            fg=GREEN
        ).pack(
            side="left",
            padx=10,
            pady=12
        )

        text = tk.Frame(
            box,
            bg=colour
        )

        text.pack(
            side="left",
            pady=12
        )

        tk.Label(
            text,
            text=heading,
            font=("Arial", 8, "bold"),
            bg=colour,
            fg=GREY
        ).pack(anchor="w")

        tk.Label(
            text,
            text=value,
            font=("Arial", 16, "bold"),
            bg=colour,
            fg=DARK
        ).pack(anchor="w")

    # ========================================================
    # ADD / EDIT WASTE
    # ========================================================

    def add_window(self, existing=None):

        win = tk.Toplevel(self)

        win.title(
            "Add Waste • TerraLoop"
            if existing is None
            else "Edit Waste • TerraLoop"
        )

        win.geometry("430x500")
        win.configure(bg=BG)
        win.resizable(False, False)

        heading = (
            "🌿 Add Waste Record"
            if existing is None
            else "✏ Edit Waste Record"
        )

        tk.Label(
            win,
            text=heading,
            font=("Arial", 20, "bold"),
            bg=BG,
            fg=DARK
        ).pack(pady=20)

        # Category
        tk.Label(
            win,
            text="Category",
            bg=BG,
            fg=GREY
        ).pack()

        cat = tk.StringVar(
            value=(
                existing.category
                if existing
                else "Plastic"
            )
        )

        tk.OptionMenu(
            win,
            cat,
            *CATEGORIES
        ).pack(pady=5)

        # Weight
        tk.Label(
            win,
            text="Weight (kg)",
            bg=BG,
            fg=GREY
        ).pack(pady=(10, 0))

        weight = tk.Entry(
            win,
            font=("Arial", 12)
        )

        weight.pack(pady=5)

        if existing:

            weight.insert(
                0,
                str(existing.weight)
            )

        # Date
        tk.Label(
            win,
            text="Date (YYYY-MM-DD)",
            bg=BG,
            fg=GREY
        ).pack(pady=(10, 0))

        record_date = tk.Entry(
            win,
            font=("Arial", 11)
        )

        record_date.pack(pady=5)

        record_date.insert(
            0,
            (
                existing.record_date
                if existing
                else str(date.today())
            )
        )

        # Recycled
        recycled = tk.BooleanVar(
            value=(
                existing.recycled
                if existing
                else False
            )
        )

        tk.Checkbutton(
            win,
            text="♻ Recycled?",
            variable=recycled,
            bg=BG,
            fg=DARK,
            activebackground=BG
        ).pack(pady=10)

        # Note
        tk.Label(
            win,
            text="Note",
            bg=BG,
            fg=GREY
        ).pack()

        note = tk.Entry(
            win,
            font=("Arial", 11)
        )

        note.pack(pady=5)

        if existing:

            note.insert(
                0,
                existing.note
            )

        # Save
        def save():

            try:

                kg = float(
                    weight.get().strip()
                )

                if kg <= 0:
                    raise ValueError

                entered_date = (
                    record_date.get().strip()
                )

                parsed_date = datetime.strptime(
                    entered_date,
                    "%Y-%m-%d"
                ).date()

                # Prevent impossible future dates
                if parsed_date > date.today():

                    messagebox.showerror(
                        "Invalid Date",
                        "Waste records cannot use a "
                        "future date."
                    )

                    return

            except ValueError:

                messagebox.showerror(
                    "Invalid Entry",
                    "Enter a valid date and a "
                    "positive weight."
                )

                return

            if existing:

                self.manager.update_record(
                    existing.record_id,
                    entered_date,
                    cat.get(),
                    kg,
                    recycled.get(),
                    note.get().strip()
                )

                messagebox.showinfo(
                    "TerraLoop",
                    "Waste record updated successfully! 🌱"
                )

            else:

                self.manager.add_record(
                    entered_date,
                    cat.get(),
                    kg,
                    recycled.get(),
                    note.get().strip()
                )

                messagebox.showinfo(
                    "TerraLoop",
                    "Waste record added successfully! 🌱"
                )

            win.destroy()
            self.dashboard()

        tk.Button(
            win,
            text="✓  SAVE RECORD",
            command=save,
            bg=GREEN,
            fg=WHITE,
            font=("Arial", 11, "bold"),
            bd=0,
            padx=25,
            pady=10,
            cursor="hand2"
        ).pack(pady=25)

    # ========================================================
    # RECORDS
    # ========================================================

    def records_window(self):

        win = tk.Toplevel(self)

        win.title(
            "TerraLoop • Waste Records"
        )

        win.geometry("950x550")
        win.configure(bg=BG)

        tk.Label(
            win,
            text="📋 Waste Records",
            font=("Arial", 21, "bold"),
            bg=BG,
            fg=DARK
        ).pack(pady=15)

        toolbar = tk.Frame(
            win,
            bg=BG
        )

        toolbar.pack(
            fill="x",
            padx=20
        )

        search = tk.Entry(
            toolbar,
            font=("Arial", 11)
        )

        search.pack(
            side="left",
            padx=5
        )

        tk.Label(
            toolbar,
            text="Category:",
            bg=BG,
            fg=GREY
        ).pack(
            side="left",
            padx=(15, 5)
        )

        category_filter = ttk.Combobox(
            toolbar,
            values=["All"] + CATEGORIES,
            state="readonly",
            width=15
        )

        category_filter.set("All")

        category_filter.pack(
            side="left",
            padx=5
        )

        columns = (
            "ID",
            "Date",
            "Category",
            "Weight",
            "Status",
            "Note"
        )

        tree = ttk.Treeview(
            win,
            columns=columns,
            show="headings",
            height=15
        )

        for col in columns:

            tree.heading(
                col,
                text=col
            )

            tree.column(
                col,
                width=130
            )

        tree.column(
            "Note",
            width=220
        )

        tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        def refresh():

            for item in tree.get_children():
                tree.delete(item)

            results = self.manager.search(
                search.get(),
                category_filter.get()
            )

            for r in results:

                tree.insert(
                    "",
                    "end",
                    values=(
                        r.record_id,
                        r.record_date,
                        r.category,
                        f"{r.weight:.1f} kg",
                        r.status(),
                        r.note
                    )
                )

        search.bind(
            "<KeyRelease>",
            lambda event: refresh()
        )

        category_filter.bind(
            "<<ComboboxSelected>>",
            lambda event: refresh()
        )

        buttons = tk.Frame(
            win,
            bg=BG
        )

        buttons.pack(
            pady=8
        )

        def selected_record():

            selection = tree.selection()

            if not selection:

                messagebox.showwarning(
                    "Select Record",
                    "Please select a record first."
                )

                return None

            values = tree.item(
                selection[0]
            )["values"]

            return int(values[0])

        def edit():

            record_id = selected_record()

            if record_id is None:
                return

            record = next(
                (
                    r for r in self.manager.records
                    if r.record_id == record_id
                ),
                None
            )

            if record:
                self.add_window(record)

        def delete():

            record_id = selected_record()

            if record_id is None:
                return

            confirm = messagebox.askyesno(
                "Delete Record",
                "Delete this waste record?"
            )

            if confirm:

                self.manager.delete_record(
                    record_id
                )

                refresh()

        tk.Button(
            buttons,
            text="✏ Edit",
            command=edit,
            bg=BLUE,
            fg=DARK,
            bd=0,
            padx=20,
            pady=7,
            cursor="hand2"
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            buttons,
            text="🗑 Delete",
            command=delete,
            bg="#F7CCCC",
            fg=DARK,
            bd=0,
            padx=20,
            pady=7,
            cursor="hand2"
        ).pack(
            side="left",
            padx=5
        )

        refresh()

    # ========================================================
    # ANALYSIS / HOTSPOT
    # ========================================================

    def analysis_window(self):

        win = tk.Toplevel(self)

        win.title(
            "TerraLoop • Waste Analysis"
        )

        win.geometry("720x650")
        win.configure(bg=BG)

        tk.Label(
            win,
            text="🔎 Waste Hotspot Analyzer",
            font=("Arial", 23, "bold"),
            bg=BG,
            fg=DARK
        ).pack(pady=15)

        period = ttk.Combobox(
            win,
            values=[
                "Last 7 Days",
                "Last 30 Days",
                "All Time"
            ],
            state="readonly",
            width=18
        )

        period.set("All Time")

        period.pack()

        content = tk.Frame(
            win,
            bg=BG
        )

        content.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=15
        )

        def refresh():

            for widget in content.winfo_children():
                widget.destroy()

            records = self.get_records_for_period(
                period.get()
            )

            analyzer = WasteAnalyzer(records)

            total = analyzer.total_waste()

            hotspot, hotspot_percent = (
                analyzer.hotspot()
            )

            if hotspot:

                tk.Label(
                    content,
                    text=f"MAIN HOTSPOT: {hotspot}",
                    font=("Arial", 17, "bold"),
                    bg=YELLOW,
                    fg=GREEN,
                    padx=20,
                    pady=10
                ).pack(pady=5)

                tk.Label(
                    content,
                    text=f"{hotspot_percent:.1f}% "
                         "of total recorded waste",
                    font=("Arial", 10),
                    bg=BG,
                    fg=GREY
                ).pack()

            else:

                tk.Label(
                    content,
                    text="No waste data for this period.",
                    font=("Arial", 12, "bold"),
                    bg=BG,
                    fg=GREY
                ).pack(pady=30)

                return

            tk.Label(
                content,
                text=f"Total Waste: {total:.2f} kg",
                font=("Arial", 13, "bold"),
                bg=BG,
                fg=DARK
            ).pack(pady=8)

            box = tk.Frame(
                content,
                bg=WHITE,
                highlightbackground="#E5E8EF",
                highlightthickness=1
            )

            box.pack(
                fill="both",
                expand=True,
                pady=10
            )

            category_data = (
                analyzer.category_breakdown()
            )

            percentages = (
                analyzer.category_percentages()
            )

            for category, kg in category_data.items():

                percentage = percentages[category]

                row = tk.Frame(
                    box,
                    bg=WHITE
                )

                row.pack(
                    fill="x",
                    padx=15,
                    pady=7
                )

                tk.Label(
                    row,
                    text=category,
                    font=("Arial", 10, "bold"),
                    bg=WHITE,
                    fg=DARK,
                    width=12,
                    anchor="w"
                ).pack(side="left")

                tk.Label(
                    row,
                    text=f"{kg:.2f} kg",
                    font=("Arial", 10),
                    bg=WHITE,
                    fg=GREY,
                    width=10
                ).pack(side="left")

                bar = ttk.Progressbar(
                    row,
                    length=230,
                    maximum=100,
                    value=percentage
                )

                bar.pack(
                    side="left",
                    padx=10
                )

                tk.Label(
                    row,
                    text=f"{percentage:.1f}%",
                    font=("Arial", 10, "bold"),
                    bg=WHITE,
                    fg=GREEN
                ).pack(side="left")

        period.bind(
            "<<ComboboxSelected>>",
            lambda event: refresh()
        )

        refresh()

    # ========================================================
    # RECOMMENDATIONS
    # ========================================================

    def recommendations_window(self):

        win = tk.Toplevel(self)

        win.title(
            "TerraLoop • Recommendations"
        )

        win.geometry("720x620")
        win.configure(bg=BG)

        tk.Label(
            win,
            text="🌱 Sustainability Recommendations",
            font=("Arial", 21, "bold"),
            bg=BG,
            fg=DARK
        ).pack(pady=20)

        tk.Label(
            win,
            text="Rule-based recommendations generated "
                 "from your actual waste data.",
            font=("Arial", 10),
            bg=BG,
            fg=GREY
        ).pack()

        analyzer = WasteAnalyzer(
            self.manager.records
        )

        engine = RecommendationEngine(
            analyzer
        )

        score_card = self.card(
            win,
            MINT
        )

        score_card.pack(
            fill="x",
            padx=30,
            pady=15
        )

        tk.Label(
            score_card,
            text=f"Sustainability Score: "
                 f"{analyzer.sustainability_score()}/100",
            font=("Arial", 14, "bold"),
            bg=MINT,
            fg=GREEN
        ).pack(
            anchor="w",
            padx=18,
            pady=10
        )

        for category, action in engine.generate():

            card = self.card(
                win,
                WHITE
            )

            card.pack(
                fill="x",
                padx=30,
                pady=6
            )

            tk.Label(
                card,
                text=category,
                font=("Arial", 12, "bold"),
                bg=WHITE,
                fg=GREEN
            ).pack(
                anchor="w",
                padx=18,
                pady=(10, 3)
            )

            tk.Label(
                card,
                text=action,
                font=("Arial", 10),
                bg=WHITE,
                fg=DARK,
                wraplength=620,
                justify="left"
            ).pack(
                anchor="w",
                padx=18,
                pady=(0, 10)
            )

    # ========================================================
    # WHAT-IF SIMULATOR
    # ========================================================

    def simulator_window(self):

        win = tk.Toplevel(self)

        win.title(
            "TerraLoop • What-If Simulator"
        )

        win.geometry("670x650")
        win.configure(bg=BG)

        tk.Label(
            win,
            text="🔮 What-If Sustainability Simulator",
            font=("Arial", 21, "bold"),
            bg=BG,
            fg=DARK
        ).pack(pady=20)

        tk.Label(
            win,
            text="Explore how reducing one category "
                 "could change your waste profile.",
            font=("Arial", 11),
            bg=BG,
            fg=GREY
        ).pack()

        tk.Label(
            win,
            text="Category",
            bg=BG,
            fg=GREY
        ).pack(pady=(20, 5))

        category = ttk.Combobox(
            win,
            values=CATEGORIES,
            state="readonly"
        )

        category.set("Plastic")

        category.pack()

        tk.Label(
            win,
            text="Reduction percentage",
            bg=BG,
            fg=GREY
        ).pack(pady=(15, 5))

        reduction = tk.Scale(
            win,
            from_=5,
            to=90,
            orient="horizontal",
            length=300,
            bg=BG,
            highlightthickness=0
        )

        reduction.set(30)

        reduction.pack()

        result = tk.Label(
            win,
            text="Run a simulation to see the projected result.",
            font=("Arial", 11),
            bg=WHITE,
            fg=DARK,
            justify="left",
            padx=20,
            pady=20
        )

        result.pack(
            fill="x",
            padx=30,
            pady=25
        )

        def simulate():

            if not self.manager.records:

                result.config(
                    text="No records available for simulation."
                )

                return

            simulator = SustainabilitySimulator(
                self.manager.records
            )

            current, future = (
                simulator.simulate_reduction(
                    category.get(),
                    reduction.get()
                )
            )

            current_total = (
                current.total_waste()
            )

            future_total = (
                future.total_waste()
            )

            current_rate = (
                current.recycling_rate()
            )

            future_rate = (
                future.recycling_rate()
            )

            current_score = (
                current.sustainability_score()
            )

            future_score = (
                future.sustainability_score()
            )

            reduction_amount = (
                current_total - future_total
            )

            result.config(
                text=
                "🔮 SIMULATION RESULT\n\n"
                f"Category: {category.get()}\n"
                f"Reduction: {reduction.get()}%\n\n"
                f"Current waste: "
                f"{current_total:.2f} kg\n"
                f"Projected waste: "
                f"{future_total:.2f} kg\n"
                f"Waste reduced: "
                f"{reduction_amount:.2f} kg\n\n"
                f"Current recycling rate: "
                f"{current_rate:.1f}%\n"
                f"Projected recycling rate: "
                f"{future_rate:.1f}%\n\n"
                f"Current score: "
                f"{current_score}/100\n"
                f"Projected score: "
                f"{future_score}/100\n\n"
                f"🌱 Potential score change: "
                f"{future_score - current_score:+d} points"
            )

        tk.Button(
            win,
            text="🔮 RUN SIMULATION",
            command=simulate,
            bg=GREEN,
            fg=WHITE,
            font=("Arial", 11, "bold"),
            bd=0,
            padx=25,
            pady=10,
            cursor="hand2"
        ).pack()

    # ========================================================
    # REPORT
    # ========================================================

    def report_window(self):

        win = tk.Toplevel(self)

        win.title(
            "TerraLoop • Sustainability Report"
        )

        win.geometry("780x700")
        win.configure(bg=BG)

        tk.Label(
            win,
            text="📄 Sustainability Report",
            font=("Arial", 22, "bold"),
            bg=BG,
            fg=DARK
        ).pack(pady=(15, 5))

        # ----------------------------------------------------
        # Period selection
        # ----------------------------------------------------

        selector = tk.Frame(
            win,
            bg=BG
        )

        selector.pack(
            fill="x",
            padx=25
        )

        tk.Label(
            selector,
            text="Report period:",
            bg=BG,
            fg=DARK,
            font=("Arial", 10, "bold")
        ).pack(side="left")

        period = ttk.Combobox(
            selector,
            values=[
                "Last 7 Days",
                "Last 30 Days",
                "All Time"
            ],
            state="readonly",
            width=18
        )

        period.set("All Time")

        period.pack(
            side="left",
            padx=10
        )

        text = tk.Text(
            win,
            font=("Consolas", 10),
            bg=WHITE,
            fg=DARK,
            bd=0,
            wrap="word"
        )

        text.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=15
        )

        # ----------------------------------------------------
        # Generate report
        # ----------------------------------------------------

        def generate_report():

            records = self.get_records_for_period(
                period.get()
            )

            analyzer = WasteAnalyzer(
                records
            )

            category, percentage = (
                analyzer.hotspot()
            )

            recommendations = (
                RecommendationEngine(
                    analyzer
                ).generate()
            )

            report = (
                "TERRALOOP 🌍\n"
                "MEASURE WASTE. CLOSE THE LOOP.\n"
                + "=" * 60
                + "\n\n"
                "SUSTAINABILITY REPORT\n"
                + "-" * 60
                + "\n"
                f"Household: "
                f"{self.household.description()}\n"
                f"Period: {period.get()}\n"
                f"Generated: "
                f"{datetime.now().strftime('%d %b %Y, %I:%M %p')}\n\n"
                f"Records analyzed: "
                f"{len(records)}\n"
                f"Total Waste: "
                f"{analyzer.total_waste():.2f} kg\n"
                f"Recycled Waste: "
                f"{analyzer.recycled_waste():.2f} kg\n"
                f"Recycling Rate: "
                f"{analyzer.recycling_rate():.1f}%\n"
                f"Sustainability Score: "
                f"{analyzer.sustainability_score()}/100\n"
                f"Grade: "
                f"{analyzer.grade()}\n\n"
            )

            report += (
                "WASTE HOTSPOT\n"
                + "-" * 60
                + "\n"
            )

            if category:

                report += (
                    f"{category} — "
                    f"{percentage:.1f}% of total waste\n\n"
                )

            else:

                report += (
                    "No waste data available for this period.\n\n"
                )

            report += (
                "CATEGORY BREAKDOWN\n"
                + "-" * 60
                + "\n"
            )

            total = analyzer.total_waste()

            for cat, kg in (
                analyzer.category_breakdown().items()
            ):

                pct = (
                    kg / total * 100
                    if total
                    else 0
                )

                report += (
                    f"{cat:<15}"
                    f"{kg:>7.2f} kg   "
                    f"{pct:>5.1f}%\n"
                )

            report += (
                "\nRECOMMENDED ACTIONS\n"
                + "-" * 60
                + "\n"
            )

            for cat, action in recommendations:

                report += (
                    f"• {cat}: {action}\n\n"
                )

            report += (
                "SDG ALIGNMENT\n"
                + "-" * 60
                + "\n"
                "SDG 11 — Sustainable Cities and Communities\n"
                "SDG 12 — Responsible Consumption and Production\n"
                "SDG 13 — Climate Action\n\n"
                "PROJECT VALUE\n"
                + "-" * 60
                + "\n"
                "TerraLoop converts household waste data "
                "into measurable insights, actionable "
                "recommendations and simulated improvement "
                "strategies.\n"
            )

            text.config(
                state="normal"
            )

            text.delete(
                "1.0",
                "end"
            )

            text.insert(
                "1.0",
                report
            )

            text.config(
                state="disabled"
            )

        # ----------------------------------------------------
        # Save report
        # ----------------------------------------------------

        def save_report():

            content = text.get(
                "1.0",
                "end-1c"
            )

            if not content.strip():

                messagebox.showwarning(
                    "No Report",
                    "Generate a report first."
                )

                return

            filename = filedialog.asksaveasfilename(
                title="Save TerraLoop Report",
                defaultextension=".txt",
                filetypes=[
                    ("Text File", "*.txt"),
                    ("All Files", "*.*")
                ]
            )

            if not filename:
                return

            try:

                with open(
                    filename,
                    "w",
                    encoding="utf-8"
                ) as file:

                    file.write(content)

                messagebox.showinfo(
                    "TerraLoop",
                    "Report saved successfully! 📄"
                )

            except OSError as error:

                messagebox.showerror(
                    "Save Error",
                    f"Could not save the report.\n\n{error}"
                )

        period.bind(
            "<<ComboboxSelected>>",
            lambda event: generate_report()
        )

        buttons = tk.Frame(
            win,
            bg=BG
        )

        buttons.pack(
            pady=(0, 15)
        )

        tk.Button(
            buttons,
            text="↻ Generate Report",
            command=generate_report,
            bg=GREEN,
            fg=WHITE,
            font=("Arial", 10, "bold"),
            bd=0,
            padx=20,
            pady=8,
            cursor="hand2"
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            buttons,
            text="💾 Save TXT",
            command=save_report,
            bg=BLUE,
            fg=DARK,
            font=("Arial", 10, "bold"),
            bd=0,
            padx=20,
            pady=8,
            cursor="hand2"
        ).pack(
            side="left",
            padx=5
        )

        generate_report()


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    app = TerraLoopApp()

    app.mainloop()

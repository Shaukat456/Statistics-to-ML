# #!/usr/bin/env python3
# """
# HYDROGEN 1s WAVEFUNCTION LAB
# =============================

# A compact, single-file educational GUI for the hydrogen atom ground state (1s).

# WHAT THIS APP TEACHES
# ---------------------
# For the hydrogen 1s ground state,

#     psi_100(r) = 1/sqrt(pi*a0^3) * exp(-r/a0)

# and the probability density is

#     |psi_100(r)|^2 = 1/(pi*a0^3) * exp(-2r/a0).

# Because the wavefunction is spherically symmetric, it depends only on r.

# The probability of finding the electron between r and r+dr is NOT simply
# |psi(r)|^2 dr. In spherical coordinates,

#     dP = |psi|^2 * dV
#        = |psi(r)|^2 * 4*pi*r^2 dr.

# Therefore the radial probability density is

#     P(r) = 4*pi*r^2 |psi(r)|^2
#          = 4*r^2/a0^3 * exp(-2r/a0),

# with

#     integral_0^infinity P(r) dr = 1.

# The most probable radius for P(r) is r = a0.

# IMPORTANT DISTINCTION
# ---------------------
# 1. Wavefunction psi:
#    Can be positive/negative/complex in general. Here 1s is real and positive.

# 2. Probability density |psi|^2:
#    Probability per unit volume.

# 3. Radial probability density P(r):
#    Probability per unit radial distance. This includes the spherical-shell
#    factor 4*pi*r^2.

# APP FEATURES
# ------------
# - Calculate psi(r) and |psi(r)|^2 at a chosen radius.
# - Show the analytical normalization value.
# - Numerically integrate |psi|^2 over a spherical volume.
# - Numerically integrate P(r) over the selected radial range.
# - Radial probability plot.
# - Wavefunction / probability-density plot.
# - 2D contour plot of |psi(x,y)|^2.
# - Adjustable Bohr radius a0 and plot range.
# - Built-in presets and reset.
# - Physics-aware input validation.
# - Clean separation between physics functions, calculations, and GUI.

# INSTALL
# -------
# Recommended Python: 3.10+

# Install dependencies:

#     pip install numpy scipy matplotlib

# Run:

#     python hydrogen_1s_lab.py

# Tkinter is normally included with Python on Windows/Linux distributions.
# On some Linux systems it may need to be installed separately.

# PROJECT STRUCTURE
# -----------------
# This intentionally remains ONE Python file, but is organized into layers:

# 1. PHYSICS MODEL
#    Pure functions: psi_1s(), probability_density(), radial_probability()

# 2. NUMERICAL CALCULATIONS
#    Normalization integrals and observable calculations.

# 3. PLOTTING
#    Matplotlib figures embedded into Tkinter.

# 4. GUI / APPLICATION
#    Inputs, buttons, cards, status bar, tabs, and event handling.

# This makes the file easy to split into modules later without changing the
# underlying physics API.

# NORMALIZATION
# -------------
# For a normalized wavefunction,

#     integral |psi|^2 dV = 1.

# For the hydrogen 1s state,

#     4*pi * integral_0^infinity |psi(r)|^2 r^2 dr = 1.

# Equivalently,

#     integral_0^infinity P(r) dr = 1.

# In the GUI, the numerical integral over the user's finite plotting range will
# usually be slightly below 1 if the range is too small. Increasing r_max makes
# it approach 1.

# WHY THE CONTOUR LOOKS LIKE A CENTRAL PEAK
# ------------------------------------------
# The contour is a 2D slice through the 3D probability density:

#     rho(x,y) = |psi(sqrt(x^2+y^2))|^2.

# It is not the complete 3D probability distribution. The actual 3D density is
# spherically symmetric, so the corresponding 3D picture would be concentric
# spheres rather than directional lobes.

# LEARNING CHECKLIST
# ------------------
# After using the app, you should be able to explain:

# - Why psi_100 depends only on r.
# - The difference between psi, |psi|^2 and P(r).
# - Why r^2 appears in the radial probability.
# - Why |psi|^2 is maximum at r=0 but P(r) is maximum at r=a0.
# - Why normalization is an integral rather than simply "squaring the wavefunction".
# - Why the contour is a 2D slice of a 3D spherically symmetric state.

# This application is educational and uses the non-relativistic hydrogen 1s
# wavefunction. It does not model spin, relativistic corrections, external
# fields, or multi-electron atoms.
# """

# from __future__ import annotations

# import math
# import tkinter as tk
# from tkinter import ttk, messagebox

# import numpy as np
# from scipy.integrate import quad
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# # ============================================================================
# # 1. PHYSICS MODEL
# # ============================================================================

# DEFAULT_A0 = 1.0  # dimensionless atomic unit: a0 = 1
# DEFAULT_RMAX = 8.0  # in units of a0
# DEFAULT_POINTS = 600


# def psi_1s(r: np.ndarray | float, a0: float = 1.0):
#     """Hydrogen ground-state (1s) wavefunction."""
#     r = np.asarray(r, dtype=float)
#     return np.exp(-r / a0) / np.sqrt(np.pi * a0**3)


# def probability_density(r: np.ndarray | float, a0: float = 1.0):
#     """Probability density |psi_1s(r)|^2."""
#     psi = psi_1s(r, a0)
#     return np.abs(psi) ** 2


# def radial_probability(r: np.ndarray | float, a0: float = 1.0):
#     """
#     Radial probability density P(r) = 4*pi*r^2*|psi(r)|^2.

#     P(r) dr is the probability of finding the electron between r and r+dr.
#     """
#     r = np.asarray(r, dtype=float)
#     return 4.0 * np.pi * r**2 * probability_density(r, a0)


# def analytical_normalization() -> float:
#     """Exact normalization integral from r=0 to infinity."""
#     return 1.0


# def numerical_normalization(a0: float, rmax: float) -> float:
#     """Numerically integrate |psi|^2 over a sphere of radius rmax."""
#     integrand = lambda r: float(radial_probability(r, a0))
#     value, _ = quad(integrand, 0.0, rmax, epsabs=1e-11, epsrel=1e-11)
#     return value


# def expectation_radius(a0: float, rmax: float) -> float:
#     """
#     Truncated numerical <r> over [0, rmax].

#     For an effectively infinite range, the exact hydrogen 1s value is 3a0/2.
#     """
#     numerator = quad(
#         lambda r: r * float(radial_probability(r, a0)),
#         0.0,
#         rmax,
#         epsabs=1e-10,
#         epsrel=1e-10,
#     )[0]
#     denominator = numerical_normalization(a0, rmax)
#     return numerator / denominator if denominator else float("nan")


# # ============================================================================
# # 2. FORMATTING / VALIDATION
# # ============================================================================


# def fmt(value: float, digits: int = 6) -> str:
#     """Human-friendly scientific/general number formatting."""
#     if not np.isfinite(value):
#         return "—"
#     if value == 0:
#         return "0"
#     if abs(value) >= 1e4 or abs(value) < 1e-4:
#         return f"{value:.{digits}e}"
#     return f"{value:.{digits}f}"


# def parse_positive(text: str, name: str) -> float:
#     try:
#         value = float(text)
#     except ValueError as exc:
#         raise ValueError(f"{name} must be a valid number.") from exc
#     if not np.isfinite(value) or value <= 0:
#         raise ValueError(f"{name} must be greater than zero.")
#     return value


# # ============================================================================
# # 3. GUI
# # ============================================================================


# class Hydrogen1SLab(tk.Tk):
#     """Main application window."""

#     BG = "#0f172a"
#     PANEL = "#111c31"
#     PANEL_2 = "#16233b"
#     BORDER = "#263653"
#     TEXT = "#e5edf8"
#     MUTED = "#93a4bd"
#     ACCENT = "#58a6ff"
#     ACCENT_2 = "#8b5cf6"
#     GOOD = "#34d399"
#     WARNING = "#fbbf24"
#     PLOT_BG = "#0d1526"

#     def __init__(self):
#         super().__init__()

#         self.title("Hydrogen 1s • Wavefunction Lab")
#         self.geometry("1320x820")
#         self.minsize(1080, 700)
#         self.configure(bg=self.BG)

#         self._configure_styles()
#         self._build_variables()
#         self._build_ui()
#         self._calculate()

#     # ---------------------------------------------------------------------
#     # Styles
#     # ---------------------------------------------------------------------

#     def _configure_styles(self):
#         style = ttk.Style(self)
#         style.theme_use("clam")

#         style.configure(
#             "TFrame",
#             background=self.BG,
#         )
#         style.configure(
#             "Panel.TFrame",
#             background=self.PANEL,
#         )
#         style.configure(
#             "TLabel",
#             background=self.BG,
#             foreground=self.TEXT,
#             font=("TkDefaultFont", 10),
#         )
#         style.configure(
#             "Panel.TLabel",
#             background=self.PANEL,
#             foreground=self.TEXT,
#             font=("TkDefaultFont", 10),
#         )
#         style.configure(
#             "Muted.TLabel",
#             background=self.PANEL,
#             foreground=self.MUTED,
#             font=("TkDefaultFont", 9),
#         )
#         style.configure(
#             "Title.TLabel",
#             background=self.BG,
#             foreground=self.TEXT,
#             font=("TkDefaultFont", 22, "bold"),
#         )
#         style.configure(
#             "Subtitle.TLabel",
#             background=self.BG,
#             foreground=self.MUTED,
#             font=("TkDefaultFont", 10),
#         )
#         style.configure(
#             "CardTitle.TLabel",
#             background=self.PANEL_2,
#             foreground=self.MUTED,
#             font=("TkDefaultFont", 9, "bold"),
#         )
#         style.configure(
#             "CardValue.TLabel",
#             background=self.PANEL_2,
#             foreground=self.TEXT,
#             font=("TkDefaultFont", 15, "bold"),
#         )
#         style.configure(
#             "TNotebook",
#             background=self.BG,
#             borderwidth=0,
#         )
#         style.configure(
#             "TNotebook.Tab",
#             background=self.PANEL,
#             foreground=self.MUTED,
#             padding=(16, 9),
#             font=("TkDefaultFont", 9, "bold"),
#         )
#         style.map(
#             "TNotebook.Tab",
#             background=[("selected", self.PANEL_2)],
#             foreground=[("selected", self.TEXT)],
#         )
#         style.configure(
#             "TButton",
#             background=self.PANEL_2,
#             foreground=self.TEXT,
#             borderwidth=0,
#             padding=(12, 9),
#             font=("TkDefaultFont", 9, "bold"),
#         )
#         style.map(
#             "TButton",
#             background=[("active", "#203251")],
#         )
#         style.configure(
#             "Accent.TButton",
#             background=self.ACCENT,
#             foreground="#07111f",
#             padding=(15, 10),
#             font=("TkDefaultFont", 9, "bold"),
#         )
#         style.map(
#             "Accent.TButton",
#             background=[("active", "#78b8ff")],
#         )
#         style.configure(
#             "TEntry",
#             fieldbackground="#0d1729",
#             foreground=self.TEXT,
#             insertcolor=self.TEXT,
#             borderwidth=1,
#             padding=8,
#         )
#         style.configure(
#             "TCombobox",
#             fieldbackground="#0d1729",
#             background="#0d1729",
#             foreground=self.TEXT,
#             arrowcolor=self.TEXT,
#             padding=7,
#         )

#     # ---------------------------------------------------------------------
#     # Variables
#     # ---------------------------------------------------------------------

#     def _build_variables(self):
#         self.a0_var = tk.StringVar(value=str(DEFAULT_A0))
#         self.rmax_var = tk.StringVar(value=str(DEFAULT_RMAX))
#         self.r_var = tk.StringVar(value="1.00")

#         self.psi_var = tk.StringVar(value="—")
#         self.density_var = tk.StringVar(value="—")
#         self.radial_var = tk.StringVar(value="—")
#         self.norm_var = tk.StringVar(value="—")
#         self.mean_r_var = tk.StringVar(value="—")
#         self.peak_r_var = tk.StringVar(value="a₀")

#         self.status_var = tk.StringVar(value="Ready")

#     # ---------------------------------------------------------------------
#     # UI
#     # ---------------------------------------------------------------------

#     def _build_ui(self):
#         header = ttk.Frame(self)
#         header.pack(fill="x", padx=28, pady=(24, 12))

#         title_box = ttk.Frame(header)
#         title_box.pack(side="left", fill="x", expand=True)

#         ttk.Label(
#             title_box,
#             text="Hydrogen 1s • Wavefunction Lab",
#             style="Title.TLabel",
#         ).pack(anchor="w")

#         ttk.Label(
#             title_box,
#             text="Calculate  ψ, |ψ|², normalization, radial probability and 2D density contours.",
#             style="Subtitle.TLabel",
#         ).pack(anchor="w", pady=(4, 0))

#         tk.Label(
#             header,
#             text="QUANTUM MECHANICS",
#             bg=self.ACCENT_2,
#             fg="white",
#             font=("TkDefaultFont", 8, "bold"),
#             padx=10,
#             pady=5,
#         ).pack(side="right", anchor="n")

#         body = ttk.Frame(self)
#         body.pack(fill="both", expand=True, padx=28, pady=(0, 18))

#         body.columnconfigure(1, weight=1)
#         body.rowconfigure(0, weight=1)

#         self._build_sidebar(body)
#         self._build_main(body)

#         status = tk.Frame(self, bg=self.PANEL, height=30)
#         status.pack(fill="x", side="bottom")
#         tk.Label(
#             status,
#             textvariable=self.status_var,
#             bg=self.PANEL,
#             fg=self.MUTED,
#             anchor="w",
#             padx=28,
#             font=("TkDefaultFont", 9),
#         ).pack(fill="both")

#     def _build_sidebar(self, parent):
#         sidebar = ttk.Frame(parent, style="Panel.TFrame", padding=18)
#         sidebar.grid(row=0, column=0, sticky="nsew", padx=(0, 14))
#         sidebar.configure(width=310)

#         tk.Label(
#             sidebar,
#             text="MODEL CONTROLS",
#             bg=self.PANEL,
#             fg=self.ACCENT,
#             font=("TkDefaultFont", 9, "bold"),
#         ).pack(anchor="w")

#         ttk.Label(
#             sidebar,
#             text="Hydrogen 1s ground state",
#             style="Panel.TLabel",
#             font=("TkDefaultFont", 15, "bold"),
#         ).pack(anchor="w", pady=(5, 2))

#         ttk.Label(
#             sidebar,
#             text="Atomic units are used by default. Set a₀ to 1 for the standard textbook form.",
#             style="Muted.TLabel",
#             wraplength=270,
#         ).pack(anchor="w", pady=(0, 18))

#         self._field(sidebar, "Bohr radius  a₀", self.a0_var)
#         self._field(sidebar, "Maximum radius  rₘₐₓ / a₀", self.rmax_var)
#         self._field(sidebar, "Evaluate at  r / a₀", self.r_var)

#         btn_row = ttk.Frame(sidebar, style="Panel.TFrame")
#         btn_row.pack(fill="x", pady=(14, 8))

#         ttk.Button(
#             btn_row,
#             text="Calculate",
#             style="Accent.TButton",
#             command=self._calculate,
#         ).pack(side="left", fill="x", expand=True, padx=(0, 5))

#         ttk.Button(
#             btn_row,
#             text="Reset",
#             command=self._reset,
#         ).pack(side="left", fill="x", expand=True, padx=(5, 0))

#         ttk.Label(
#             sidebar,
#             text="Quick range",
#             style="Muted.TLabel",
#         ).pack(anchor="w", pady=(13, 5))

#         presets = ttk.Frame(sidebar, style="Panel.TFrame")
#         presets.pack(fill="x")

#         for label, value in [("4 a₀", "4"), ("8 a₀", "8"), ("12 a₀", "12")]:
#             ttk.Button(
#                 presets,
#                 text=label,
#                 command=lambda v=value: self._set_rmax(v),
#             ).pack(side="left", fill="x", expand=True, padx=2)

#         ttk.Separator(sidebar).pack(fill="x", pady=20)

#         tk.Label(
#             sidebar,
#             text="CORE EQUATIONS",
#             bg=self.PANEL,
#             fg=self.ACCENT,
#             font=("TkDefaultFont", 9, "bold"),
#         ).pack(anchor="w")

#         equations = [
#             "ψ₁₀₀(r) = exp(−r/a₀) / √(πa₀³)",
#             "|ψ|² = exp(−2r/a₀) / (πa₀³)",
#             "P(r) = 4πr²|ψ|²",
#             "∫₀∞ P(r)dr = 1",
#         ]

#         for eq in equations:
#             tk.Label(
#                 sidebar,
#                 text=eq,
#                 bg=self.PANEL,
#                 fg=self.TEXT,
#                 anchor="w",
#                 justify="left",
#                 font=("TkDefaultFont", 9),
#             ).pack(fill="x", pady=3)

#         ttk.Separator(sidebar).pack(fill="x", pady=18)

#         ttk.Label(
#             sidebar,
#             text="Physics note",
#             style="Muted.TLabel",
#         ).pack(anchor="w")

#         ttk.Label(
#             sidebar,
#             text="|ψ|² is probability per unit volume. P(r) includes the spherical-shell factor 4πr², so P(r)dr is a radial probability.",
#             style="Muted.TLabel",
#             wraplength=270,
#             justify="left",
#         ).pack(anchor="w", pady=(4, 0))

#     def _field(self, parent, label, variable):
#         ttk.Label(parent, text=label, style="Panel.TLabel").pack(
#             anchor="w", pady=(9, 5)
#         )
#         entry = ttk.Entry(parent, textvariable=variable)
#         entry.pack(fill="x")
#         entry.bind("<Return>", lambda _event: self._calculate())

#     def _build_main(self, parent):
#         main = ttk.Frame(parent)
#         main.grid(row=0, column=1, sticky="nsew")
#         main.rowconfigure(1, weight=1)
#         main.columnconfigure(0, weight=1)

#         cards = ttk.Frame(main)
#         cards.grid(row=0, column=0, sticky="ew", pady=(0, 14))
#         for i in range(5):
#             cards.columnconfigure(i, weight=1)

#         card_specs = [
#             ("ψ(r)", self.psi_var),
#             ("|ψ(r)|²", self.density_var),
#             ("P(r)", self.radial_var),
#             ("Normalization", self.norm_var),
#             ("Peak radius", self.peak_r_var),
#         ]

#         for i, (label, variable) in enumerate(card_specs):
#             card = tk.Frame(
#                 cards,
#                 bg=self.PANEL_2,
#                 highlightbackground=self.BORDER,
#                 highlightthickness=1,
#             )
#             card.grid(row=0, column=i, sticky="ew", padx=(0 if i == 0 else 5, 0))
#             tk.Label(
#                 card,
#                 text=label,
#                 bg=self.PANEL_2,
#                 fg=self.MUTED,
#                 font=("TkDefaultFont", 8, "bold"),
#             ).pack(anchor="w", padx=12, pady=(9, 1))
#             tk.Label(
#                 card,
#                 textvariable=variable,
#                 bg=self.PANEL_2,
#                 fg=self.TEXT,
#                 font=("TkDefaultFont", 13, "bold"),
#             ).pack(anchor="w", padx=12, pady=(0, 9))

#         notebook = ttk.Notebook(main)
#         notebook.grid(row=1, column=0, sticky="nsew")

#         self.radial_tab = ttk.Frame(notebook, style="Panel.TFrame")
#         self.contour_tab = ttk.Frame(notebook, style="Panel.TFrame")
#         self.details_tab = ttk.Frame(notebook, style="Panel.TFrame")

#         notebook.add(self.radial_tab, text="  Radial probability  ")
#         notebook.add(self.contour_tab, text="  2D contour  ")
#         notebook.add(self.details_tab, text="  Calculation details  ")

#         self._build_radial_plot()
#         self._build_contour_plot()
#         self._build_details()

#     # ---------------------------------------------------------------------
#     # Plot setup
#     # ---------------------------------------------------------------------

#     def _make_figure(self, title):
#         fig = Figure(figsize=(7, 5), dpi=100, facecolor=self.PLOT_BG)
#         ax = fig.add_subplot(111)
#         ax.set_facecolor(self.PLOT_BG)
#         ax.set_title(title, color=self.TEXT, fontsize=12, fontweight="bold", pad=12)
#         ax.tick_params(colors=self.MUTED, labelsize=8)
#         for spine in ax.spines.values():
#             spine.set_color(self.BORDER)
#         ax.grid(True, alpha=0.12)
#         ax.set_xlabel("r / a₀", color=self.MUTED)
#         return fig, ax

#     def _embed_figure(self, parent, fig):
#         canvas = FigureCanvasTkAgg(fig, master=parent)
#         canvas.get_tk_widget().pack(fill="both", expand=True, padx=12, pady=12)
#         return canvas

#     def _build_radial_plot(self):
#         self.radial_fig, self.radial_ax = self._make_figure(
#             "Hydrogen 1s radial probability"
#         )
#         self.radial_ax.set_ylabel("P(r)", color=self.MUTED)
#         self.radial_canvas = self._embed_figure(self.radial_tab, self.radial_fig)

#     def _build_contour_plot(self):
#         self.contour_fig = Figure(figsize=(7, 5), dpi=100, facecolor=self.PLOT_BG)
#         self.contour_ax = self.contour_fig.add_subplot(111)
#         self.contour_ax.set_facecolor(self.PLOT_BG)
#         self.contour_canvas = self._embed_figure(self.contour_tab, self.contour_fig)

#     def _build_details(self):
#         frame = tk.Frame(self.details_tab, bg=self.PANEL, padx=25, pady=25)
#         frame.pack(fill="both", expand=True)

#         tk.Label(
#             frame,
#             text="What the calculator is actually computing",
#             bg=self.PANEL,
#             fg=self.TEXT,
#             font=("TkDefaultFont", 16, "bold"),
#         ).pack(anchor="w", pady=(0, 12))

#         details = (
#             "1. Wavefunction\n"
#             "   ψ(r) = 1/√(πa₀³) · exp(−r/a₀)\n\n"
#             "2. Probability density\n"
#             "   ρ(r) = |ψ(r)|²\n"
#             "   This tells you probability per unit volume.\n\n"
#             "3. Radial probability\n"
#             "   P(r) = 4πr²ρ(r)\n"
#             "   This tells you the probability distribution with respect to radius.\n\n"
#             "4. Normalization\n"
#             "   ∫ |ψ|² dV = 4π∫₀∞ r²|ψ(r)|²dr = 1\n\n"
#             "5. Ground-state result\n"
#             "   P(r) reaches its maximum at r = a₀.\n"
#             "   The exact expectation value is ⟨r⟩ = 3a₀/2."
#         )

#         tk.Label(
#             frame,
#             text=details,
#             bg=self.PANEL,
#             fg=self.MUTED,
#             justify="left",
#             anchor="nw",
#             font=("TkDefaultFont", 10),
#         ).pack(anchor="w")

#     # ---------------------------------------------------------------------
#     # Actions
#     # ---------------------------------------------------------------------

#     def _set_rmax(self, value):
#         self.rmax_var.set(value)
#         self._calculate()

#     def _reset(self):
#         self.a0_var.set(str(DEFAULT_A0))
#         self.rmax_var.set(str(DEFAULT_RMAX))
#         self.r_var.set("1.00")
#         self._calculate()

#     def _calculate(self):
#         try:
#             a0 = parse_positive(self.a0_var.get(), "a₀")
#             rmax = parse_positive(self.rmax_var.get(), "rₘₐₓ")
#             r = float(self.r_var.get())
#             if not np.isfinite(r) or r < 0:
#                 raise ValueError("r must be zero or greater.")
#             if r > rmax:
#                 raise ValueError("Evaluation radius r cannot exceed rₘₐₓ.")

#             psi = float(psi_1s(r, a0))
#             density = float(probability_density(r, a0))
#             radial = float(radial_probability(r, a0))
#             norm = numerical_normalization(a0, rmax)
#             mean_r = expectation_radius(a0, rmax)

#             self.psi_var.set(fmt(psi))
#             self.density_var.set(fmt(density))
#             self.radial_var.set(fmt(radial))
#             self.norm_var.set(f"{norm:.8f}")
#             self.mean_r_var.set(f"{mean_r:.6f}")

#             self._update_radial_plot(a0, rmax, r)
#             self._update_contour_plot(a0, rmax)

#             if abs(norm - 1.0) < 1e-5:
#                 status = f"Normalized over 0 ≤ r ≤ {rmax:g}a₀ • numerical error < 1e−5"
#             else:
#                 status = (
#                     f"Finite-range normalization = {norm:.8f}. "
#                     "Increase rₘₐₓ to approach 1."
#                 )

#             self.status_var.set(status)

#         except ValueError as exc:
#             self.status_var.set("Input error")
#             messagebox.showerror("Check your inputs", str(exc))

#     # ---------------------------------------------------------------------
#     # Plot updates
#     # ---------------------------------------------------------------------

#     def _update_radial_plot(self, a0, rmax, selected_r):
#         x = np.linspace(0.0, rmax, DEFAULT_POINTS)
#         p = radial_probability(x, a0)
#         density = probability_density(x, a0)

#         ax = self.radial_ax
#         ax.clear()
#         ax.set_facecolor(self.PLOT_BG)

#         ax.plot(x / a0, p * a0, linewidth=2.2, label="P(r)")

#         # Show the probability density too, scaled only for visual comparison.
#         # The scale is explicitly labeled, so this is not presented as the same
#         # physical quantity.
#         density_scale = np.max(p) / max(np.max(density), 1e-30)
#         ax.plot(
#             x / a0,
#             density * density_scale * a0,
#             linestyle="--",
#             linewidth=1.6,
#             alpha=0.75,
#             label="|ψ|² (scaled for display)",
#         )

#         ax.axvline(
#             1.0,
#             linestyle=":",
#             linewidth=1.4,
#             label="most probable r = a₀",
#         )

#         if selected_r <= rmax:
#             selected_p = float(radial_probability(selected_r, a0))
#             ax.scatter(
#                 [selected_r / a0],
#                 [selected_p * a0],
#                 s=45,
#                 zorder=5,
#                 label=f"selected r = {selected_r/a0:.2f}a₀",
#             )

#         ax.set_title(
#             "Hydrogen 1s radial probability",
#             color=self.TEXT,
#             fontsize=12,
#             fontweight="bold",
#         )
#         ax.set_xlabel("r / a₀", color=self.MUTED)
#         ax.set_ylabel("Radial probability density", color=self.MUTED)
#         ax.tick_params(colors=self.MUTED, labelsize=8)
#         ax.grid(True, alpha=0.12)

#         for spine in ax.spines.values():
#             spine.set_color(self.BORDER)

#         legend = ax.legend(frameon=False, fontsize=8, loc="upper right")
#         for text in legend.get_texts():
#             text.set_color(self.MUTED)

#         self.radial_fig.tight_layout()
#         self.radial_canvas.draw_idle()

#     def _update_contour_plot(self, a0, rmax):
#         # A 2D slice from -rmax to +rmax.
#         n = 260
#         x = np.linspace(-rmax, rmax, n)
#         y = np.linspace(-rmax, rmax, n)
#         X, Y = np.meshgrid(x, y)
#         R = np.sqrt(X**2 + Y**2)

#         Z = probability_density(R, a0)

#         ax = self.contour_ax
#         ax.clear()
#         ax.set_facecolor(self.PLOT_BG)

#         # Log contours make the exponentially decaying tails visible while
#         # preserving the physical quantity being plotted.
#         zmax = float(np.max(Z))
#         positive = Z[Z > 0]
#         zmin = max(float(np.min(positive)), zmax * 1e-7)

#         levels = np.geomspace(zmin, zmax, 14)

#         contour = ax.contourf(
#             X / a0,
#             Y / a0,
#             Z,
#             levels=levels,
#         )
#         ax.contour(
#             X / a0,
#             Y / a0,
#             Z,
#             levels=levels,
#             linewidths=0.35,
#             alpha=0.55,
#         )

#         # Remove old colorbars safely by recreating the figure's colorbar.
#         if hasattr(self, "_colorbar") and self._colorbar is not None:
#             try:
#                 self._colorbar.remove()
#             except Exception:
#                 pass

#         self._colorbar = self.contour_fig.colorbar(
#             contour,
#             ax=ax,
#             pad=0.02,
#             shrink=0.88,
#         )
#         self._colorbar.set_label("|ψ|²", color=self.MUTED)
#         self._colorbar.ax.tick_params(colors=self.MUTED, labelsize=7)

#         ax.set_title(
#             "|ψ(x,y)|² — 2D slice of the spherical 1s density",
#             color=self.TEXT,
#             fontsize=12,
#             fontweight="bold",
#         )
#         ax.set_xlabel("x / a₀", color=self.MUTED)
#         ax.set_ylabel("y / a₀", color=self.MUTED)
#         ax.tick_params(colors=self.MUTED, labelsize=8)
#         ax.set_aspect("equal", adjustable="box")

#         for spine in ax.spines.values():
#             spine.set_color(self.BORDER)

#         self.contour_fig.tight_layout()
#         self.contour_canvas.draw_idle()


# def main():
#     app = Hydrogen1SLab()
#     app.mainloop()


# if __name__ == "__main__":
#     main()

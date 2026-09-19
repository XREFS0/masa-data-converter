"""
MASA DataMorph Converter: High-Precision Data Rate & Storage Matrix
Developer: MASA
"""

import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class MasaDataConverter(ctk.CTk):
    UNIT_MAP = {
        "Bit/s (bps)": 1.0,
        "Kilobit/s (Kbps)": 1e3,
        "Kibibit/s (Kibps)": 1024.0,
        "Kilobyte/s (KB/s)": 8e3,
        "Megabit/s (Mbps)": 1e6,
        "Mebibit/s (Mibps)": 1048576.0,
        "Megabyte/s (MB/s)": 8e6,
        "Gigabit/s (Gbps)": 1e9,
        "Gibibit/s (Gibps)": 1073741824.0,
        "Gigabyte/s (GB/s)": 8e9,
        "Terabit/s (Tbps)": 1e12,
        "Terabyte/s (TB/s)": 8e12,
    }

    def __init__(self):
        super().__init__()

        self.title("MASA DataMorph Converter")
        self.geometry("520x580")
        self.resizable(False, False)
        self.configure(fg_color="#0A0E17")

        self.units = list(self.UNIT_MAP.keys())
        self.from_var = ctk.StringVar(value="Megabyte/s (MB/s)")
        self.to_var = ctk.StringVar(value="Megabit/s (Mbps)")

        self._build_ui()
        self._calculate()

    def _build_ui(self):
        header = ctk.CTkFrame(self, fg_color="#121826", corner_radius=14)
        header.pack(fill="x", padx=20, pady=(20, 15))

        title = ctk.CTkLabel(
            header,
            text="MASA DATAMORPH MATRIX",
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="#38BDF8",
        )
        title.pack(pady=(12, 2))

        subtitle = ctk.CTkLabel(
            header,
            text="Universal Bandwidth & Data Transfer Rate Converter",
            font=ctk.CTkFont(size=11),
            text_color="#94A3B8",
        )
        subtitle.pack(pady=(0, 12))

        calc_card = ctk.CTkFrame(self, fg_color="#121826", corner_radius=16)
        calc_card.pack(fill="x", padx=20, pady=5)

        lbl_val = ctk.CTkLabel(
            calc_card,
            text="TRANSFER QUANTITY",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="#94A3B8",
        )
        lbl_val.pack(anchor="w", padx=16, pady=(15, 2))

        self.entry_val = ctk.CTkEntry(
            calc_card,
            placeholder_text="100.0",
            font=ctk.CTkFont(family="Consolas", size=16),
            height=40,
            corner_radius=10,
        )
        self.entry_val.pack(fill="x", padx=16, pady=(0, 12))
        self.entry_val.insert(0, "100")
        self.entry_val.bind("<KeyRelease>", lambda _: self._calculate())

        units_grid = ctk.CTkFrame(calc_card, fg_color="transparent")
        units_grid.pack(fill="x", padx=16, pady=(0, 15))
        units_grid.grid_columnconfigure((0, 1), weight=1)

        lbl_f = ctk.CTkLabel(
            units_grid, text="FROM UNIT", font=ctk.CTkFont(size=11, weight="bold"), text_color="#94A3B8"
        )
        lbl_f.grid(row=0, column=0, sticky="w", pady=(0, 2))

        self.menu_f = ctk.CTkOptionMenu(
            units_grid,
            values=self.units,
            variable=self.from_var,
            command=lambda _: self._calculate(),
            fg_color="#0284C7",
            button_color="#0369A1",
            corner_radius=8,
        )
        self.menu_f.grid(row=1, column=0, sticky="ew", padx=(0, 6))

        lbl_t = ctk.CTkLabel(
            units_grid, text="TO UNIT", font=ctk.CTkFont(size=11, weight="bold"), text_color="#94A3B8"
        )
        lbl_t.grid(row=0, column=1, sticky="w", pady=(0, 2))

        self.menu_t = ctk.CTkOptionMenu(
            units_grid,
            values=self.units,
            variable=self.to_var,
            command=lambda _: self._calculate(),
            fg_color="#0284C7",
            button_color="#0369A1",
            corner_radius=8,
        )
        self.menu_t.grid(row=1, column=1, sticky="ew", padx=(6, 0))

        display_card = ctk.CTkFrame(self, fg_color="#121826", corner_radius=16)
        display_card.pack(fill="both", expand=True, padx=20, pady=(12, 20))

        self.lbl_res = ctk.CTkLabel(
            display_card,
            text="800.0",
            font=ctk.CTkFont(family="Consolas", size=38, weight="bold"),
            text_color="#38BDF8",
        )
        self.lbl_res.pack(pady=(25, 4))

        self.lbl_formula = ctk.CTkLabel(
            display_card, text="", font=ctk.CTkFont(size=12), text_color="#94A3B8"
        )
        self.lbl_formula.pack(pady=(0, 20))

        btn_swap = ctk.CTkButton(
            display_card,
            text="⇄ Invert Units",
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color="#1E293B",
            hover_color="#334155",
            corner_radius=8,
            command=self._swap,
        )
        btn_swap.pack(side="bottom", pady=15)

    def _swap(self):
        f = self.from_var.get()
        t = self.to_var.get()
        self.from_var.set(t)
        self.to_var.set(f)
        self._calculate()

    def _calculate(self):
        raw = self.entry_val.get().strip()
        if not raw:
            self.lbl_res.configure(text="0")
            return
        try:
            val = float(raw)
        except ValueError:
            self.lbl_res.configure(text="Invalid Literal")
            return

        f_factor = self.UNIT_MAP[self.from_var.get()]
        t_factor = self.UNIT_MAP[self.to_var.get()]
        bps = val * f_factor
        converted = bps / t_factor

        formatted = f"{converted:.6g}"
        self.lbl_res.configure(text=formatted)
        self.lbl_formula.configure(text=f"{val:g} {self.from_var.get()} = {formatted} {self.to_var.get()}")


if __name__ == "__main__":
    app = MasaDataConverter()
    app.mainloop()

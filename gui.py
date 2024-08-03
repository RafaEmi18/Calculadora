import customtkinter as ctk
import sympy as sp
from utils import preprocess_input
from integration_utils import integrate_function
from derivation_utils import derive_function
from latex_utils import render_latex

class CalculatorApp:
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("Calculadora")

        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        self.theme_button = ctk.CTkButton(self.root, text="🌓", width=30, command=self.toggle_theme)
        self.theme_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

        self.title_label = ctk.CTkLabel(self.main_frame, text="Calculadora de Derivadas e Integrales", font=("Arial", 18))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        self.integral_button = ctk.CTkButton(self.main_frame, text="Integrales", command=lambda: self.switch_calculator("integral"))
        self.integral_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.derivative_button = ctk.CTkButton(self.main_frame, text="Derivadas", command=lambda: self.switch_calculator("derivative"))
        self.derivative_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.calculator_label = ctk.CTkLabel(self.main_frame, text="", font=("Arial", 16))
        self.calculator_label.grid(row=2, column=0, columnspan=2, pady=(10, 5))

        self.entry = ctk.CTkEntry(self.main_frame, width=300)
        self.entry.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        self.entry.bind("<KeyRelease>", self.update_display)

        self.go_button = ctk.CTkButton(self.main_frame, text="Calcular", width=100, command=self.calculate)
        self.go_button.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        self.input_display = ctk.CTkLabel(self.main_frame, text="")
        self.input_display.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        self.result_display = ctk.CTkLabel(self.main_frame, text="")
        self.result_display.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)

        self.current_calculator = None
        self.switch_calculator("integral")

    def toggle_theme(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")

    def switch_calculator(self, calculator_type):
        self.current_calculator = calculator_type
        if calculator_type == "integral":
            self.calculator_label.configure(text="Calculadora de Integrales")
            self.go_button.configure(text="Integrar")
        else:
            self.calculator_label.configure(text="Calculadora de Derivadas")
            self.go_button.configure(text="Derivar")
        self.entry.delete(0, 'end')
        self.input_display.configure(image=None, text="")
        self.result_display.configure(image=None, text="")

    def update_display(self, *args):
        input_text = self.entry.get()
        try:
            if input_text:
                processed_text = preprocess_input(input_text)
                x = sp.Symbol('x')
                expr = sp.sympify(processed_text)
                latex_expr = sp.latex(expr)
                if self.current_calculator == "integral":
                    full_latex_expr = r'\int ' + latex_expr + r' \,dx'
                else:
                    full_latex_expr = r'\frac{d}{dx}(' + latex_expr + r')'
                render_latex(full_latex_expr, self.input_display)
            else:
                self.input_display.configure(image=None, text="")
        except (sp.SympifyError, TypeError) as e:
            self.input_display.configure(image=None, text="")

    def calculate(self):
        input_text = self.entry.get()
        try:
            if self.current_calculator == "integral":
                result = integrate_function(input_text)
                result_with_c = result + " + C"
                render_latex(result_with_c, self.result_display)
            else:
                result = derive_function(input_text)
                render_latex(result, self.result_display)
        except Exception as e:
            self.result_display.configure(image=None, text="")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
from matplotlib.figure import Figure
from PIL import Image
import io
import customtkinter as ctk

def render_latex(latex_str, label):
    fig = Figure(figsize=(4, 0.5), dpi=100)
    fig.patch.set_facecolor('none')
    ax = fig.add_subplot(111)
    ax.axis('off')
    ax.text(0, 0.5, f"${latex_str}$", fontsize=18, va='center')

    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.1, transparent=True)
    buf.seek(0)
    img = Image.open(buf)
    photo = ctk.CTkImage(light_image=img, dark_image=img, size=img.size)
    
    label.configure(image=photo)
    label.image = photo
import os
import sys
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

from Functions import utilities as f

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../models/'))
from Functions.models import utilFunctions as UF

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../transformations/'))


def pitch_interface(master):
    # CONFIGURE THE PITCH SHIFTING FRAME

    # Configure grid layout (3x7)
    master.pitch_frame.rowconfigure(1, weight=0)

    # TITLE
    master.pitch_frame.frame_title = customtkinter.CTkLabel(master=master.pitch_frame,
                                                            text="Pitch shifting",
                                                            text_font=("Roboto Medium", -30),
                                                            fg_color=("white", "gray18"),
                                                            width=30)  # font name and size in px

    master.pitch_frame.frame_title.grid(row=0, column=0, pady=(15, 0), padx=40, sticky="w")

    # INPUT FILE 1
    master.pitch_frame.file_label = customtkinter.CTkLabel(master=master.pitch_frame,
                                                           text="File:",
                                                           text_font=("Roboto Medium", -16),
                                                           fg_color=("white", "gray30"),
                                                           width=30)  # font name and size in px

    master.pitch_frame.file_label.grid(row=1, column=0, pady=0, padx=50, sticky="w")

    master.pitch_frame.filelocation_pitch = customtkinter.CTkEntry(master=master.pitch_frame,
                                                                   width=10,
                                                                   placeholder_text="Path to the first input file")  # TEXTBOX TO PRINT PATH OF THE SOUND FILE

    master.pitch_frame.filelocation_pitch.grid(row=1, column=0, pady=20, padx=(120, 650), sticky="we")
    master.pitch_frame.filelocation_pitch.focus_set()

    # Button to browse the input file 1
    master.pitch_frame.open_file_pitch = customtkinter.CTkButton(master.pitch_frame,
                                                                 text="...", width=3,
                                                                 command=lambda: f.browse_file1(master, 3))

    master.pitch_frame.open_file_pitch.grid(row=1, column=0, sticky="e", padx=(70, 610), pady=5)

    # Button to play the input file 1
    master.pitch_frame.preview_pitch = customtkinter.CTkButton(master.pitch_frame,
                                                               text="Play!", width=3,
                                                               command=lambda: UF.wavplay(
                                                                   master.pitch_frame.filelocation_pitch.get()),
                                                               fg_color=("gray75", "gray30"),
                                                               hover_color="green")

    master.pitch_frame.preview_pitch.grid(row=1, column=0, columnspan=3, sticky="e", padx=(150, 550), pady=20)

    # Draw the audio plot
    fig4 = Figure(figsize=(16, 9), dpi=100)
    fig4.set_facecolor('#2e2e2e')
    a4 = fig4.add_subplot(111)
    data = np.zeros(2)
    a4.plot(data)
    a4.axis('off')
    canvas4 = FigureCanvasTkAgg(fig4, master.pitch_frame)
    canvas4.draw()
    canvas4.get_tk_widget().configure(background='black', width=720, height=200)
    canvas4.get_tk_widget().grid(row=2, column=0, sticky="w", padx=(20, 580), pady=(0, 0))

    # Define the style
    style = ttk.Style()
    style.configure("TScale", background="gray18")

    # Create an slider space
    master.pitch_frame.label_tone = customtkinter.CTkLabel(master=master.pitch_frame,
                                                           text="Tone scale",
                                                           text_font=("Roboto Medium", -15),
                                                           fg_color=("white", "gray30"),
                                                           width=30)  # font name and size in px

    master.pitch_frame.label_tone.grid(row=3, column=0, pady=(20, 0), padx=50, sticky="nw")

    # slider current value
    master.pitch_frame.current_value = tk.DoubleVar()

    def slider16_changed(event):
        master.pitch_frame.value_number.configure(text='{: .2f}'.format(master.pitch_frame.current_value.get()))

    # Slider
    master.pitch_frame.title_slider = ttk.Scale(master.pitch_frame,
                                                from_=-12,
                                                to=12,
                                                length=410,
                                                orient=HORIZONTAL,
                                                style="TScale",
                                                command=slider16_changed,
                                                variable=master.pitch_frame.current_value)

    master.pitch_frame.title_slider.grid(row=3, column=0, pady=25, padx=170, sticky="w")

    # Right limit
    master.pitch_frame.right_limit_pitch = customtkinter.CTkLabel(master=master.pitch_frame,
                                                                  text="+12.00 ST",
                                                                  text_font=("Roboto Medium", -11),
                                                                  background="gray18",
                                                                  foreground="white")

    master.pitch_frame.right_limit_pitch.grid(row=3, column=0, pady=(45, 0), padx=510, sticky="nw")

    # Left limit
    master.pitch_frame.left_limit_pitch = customtkinter.CTkLabel(master=master.pitch_frame,
                                                                 text="-12.00 ST",
                                                                 text_font=("Roboto Medium", -11),
                                                                 background="gray18",
                                                                 foreground="white")

    master.pitch_frame.left_limit_pitch.grid(row=3, column=0, pady=(45, 0), padx=120, sticky="w")

    # Value label
    master.pitch_frame.value_label = customtkinter.CTkLabel(master=master.pitch_frame,
                                                            text="Value:",
                                                            text_font=("Roboto Medium", -12),
                                                            fg_color=("white", "gray30"),
                                                            width=30)  # font name and size in px

    master.pitch_frame.value_label.grid(row=3, column=0, pady=(7, 0), padx=630, sticky="e")

    # Value  number
    master.pitch_frame.value_number = ttk.Label(master.pitch_frame,
                                                text='{: .2f}'.format(master.pitch_frame.current_value.get()),
                                                background="gray18",
                                                justify="center",
                                                foreground="white")

    master.pitch_frame.value_number.grid(row=3, column=0, pady=(7, 0), padx=580, sticky='e')

    # Button to apply the transformation
    master.pitch_frame.apply_button = customtkinter.CTkButton(master.pitch_frame,
                                                              text="Apply transformation", width=3,
                                                              command=lambda: f.shifting(master, 2))

    master.pitch_frame.apply_button.grid(row=6, column=0, sticky="e", padx=(70, 550), pady=5)

    # Button to play the result
    master.pitch_frame.play_result_button = customtkinter.CTkButton(master.pitch_frame,
                                                                    text="▶", width=3,
                                                                    command=lambda: f.play_song(master.y3, 44100),
                                                                    fg_color=("gray75", "gray30"))

    master.pitch_frame.play_result_button.grid(row=6, column=0, sticky="s", padx=(100, 400), pady=0)

    # Button to stop the result
    master.pitch_frame.stop_result_button = customtkinter.CTkButton(master.pitch_frame,
                                                                    text="II", width=3,
                                                                    command=lambda: f.stop_song(master.y3),
                                                                    fg_color=("gray75", "gray30"))

    master.pitch_frame.stop_result_button.grid(row=6, column=0, sticky="w", padx=(100, 440), pady=0)

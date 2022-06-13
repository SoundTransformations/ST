import os
import sys
from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Functions import utilities as f

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../models/'))
from Functions.models import utilFunctions as UF
from Functions.models import dftModel as DFT

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../transformations/'))
from Functions.transformations import stftTransformations as stft

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../Functions/'))

def equalizer_interface(master):

    ## CONFIGURE THE EQUALIZER FRAME

    # Configure grid layout (3x7)
    master.equalizer_frame.rowconfigure(1, weight=0)


    master.equalizer_frame.frame_title = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="Equalizer",
                                            text_font=("Roboto Medium", -30),
                                            fg_color=("white", "gray18"),
                                            width=30)  # font name and size in px

    master.equalizer_frame.frame_title.grid(row=0, column=0, pady=(15,0), padx=40, sticky="w")


    ## INPUT FILE 1
    master.equalizer_frame.file_label = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="File:",
                                            text_font=("Roboto Medium", -16),
                                            fg_color=("white", "gray30"),
                                            width=30)  # font name and size in px

    master.equalizer_frame.file_label.grid(row=1, column=0, pady=0, padx=50, sticky="w")

    master.equalizer_frame.filelocation1 = customtkinter.CTkEntry(master=master.equalizer_frame,
                                                                  width=10,
                                                                  placeholder_text="Path to the first input file")  # TEXTBOX TO PRINT PATH OF THE SOUND FILE

    master.equalizer_frame.filelocation1.grid(row=1, column=0, pady=20, padx=(110, 480), sticky="we")
    master.equalizer_frame.filelocation1.focus_set()



    # Button to browse the input file 1
    master.equalizer_frame.open_file1 = customtkinter.CTkButton(master.equalizer_frame,
                                         text="Import", width=3,
                                         command= lambda: f.browse_file1(master,1))

    master.equalizer_frame.open_file1.grid(row=1, column=0, sticky="e", padx=(70, 410), pady=5)


    #============= SLIDERS of the EQUALIZER =======================

    # Define the style
    style = ttk.Style()
    style.configure("TScale", background="gray18")

    # Create an slider space

    master.equalizer_frame.freq1_label = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="32 Hz",
                                            text_font=("Roboto Medium", -12),
                                            fg_color=("white", "gray30"),
                                            width=30)  # font name and size in px

    master.equalizer_frame.freq1_label.grid(row=2, column=0, pady=(15,0), padx=50, sticky="nw")

    # slider current value
    master.equalizer_frame.s1_current_value = tk.DoubleVar()

    def slider1_changed(event):
        master.equalizer_frame.s1_value_label.configure(text='{: .2f}'.format(master.equalizer_frame.s1_current_value.get()))

    # Slider
    master.equalizer_frame.slider_1 = ttk.Scale(master.equalizer_frame,
                                from_=0,
                                to=-60,
                                orient=VERTICAL,
                                style="TScale",
                                command= slider1_changed,
                                variable=master.equalizer_frame.s1_current_value)

    master.equalizer_frame.slider_1.grid(row=3, column=0, pady=10, padx=65, sticky="w")

    # Value label
    master.equalizer_frame.s1_value_label = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.equalizer_frame.s1_current_value.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.equalizer_frame.s1_value_label.grid(row=4, column=0, pady=0, padx=61, sticky='sw')

    # Button to reset the slider
    master.equalizer_frame.btn_reset1 = customtkinter.CTkButton(master.equalizer_frame,
                                     text="R",
                                     width=1,
                                     text_font=("Roboto Medium", -9),
                                     height =1,
                                     fg_color = "gray40",
                                     command=lambda: f.reset_slider1(master))

    master.equalizer_frame.btn_reset1.grid(row=5, column=0, pady = (5,50), padx=62, sticky = 'sw')


    ## Create an slider space

    master.equalizer_frame.freq2_label = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="64 Hz",
                                            text_font=("Roboto Medium", -12),
                                            fg_color=("white", "gray30"),
                                            width=30)

    master.equalizer_frame.freq2_label.grid(row=2, column=0, pady=(15,0), padx=110, sticky="nw")

    # Slider current value
    master.equalizer_frame.s2_current_value = tk.DoubleVar()

    def slider2_changed(event):
        master.equalizer_frame.s2_value_label.configure(text='{: .2f}'.format(master.equalizer_frame.s2_current_value.get()))

    # Slider
    master.equalizer_frame.slider_2 = ttk.Scale(master.equalizer_frame,
                                from_=0,
                                to=-60,
                                orient=VERTICAL,
                                style="TScale",
                                command= slider2_changed,
                                variable=master.equalizer_frame.s2_current_value)

    master.equalizer_frame.slider_2.grid(row=3, column=0, pady=10, padx=122, sticky="w")

    # Value label
    master.equalizer_frame.s2_value_label = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.equalizer_frame.s2_current_value.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.equalizer_frame.s2_value_label.grid(row=4, column=0, pady=0, padx=119, sticky='sw')

    # Button to reset the slider
    master.equalizer_frame.btn_reset2 = customtkinter.CTkButton(master.equalizer_frame,
                                     text="R",
                                     width=1,
                                     text_font=("Roboto Medium", -9),
                                     height=1,
                                     fg_color="gray40",
                                     command=lambda: f.reset_slider2(master))

    master.equalizer_frame.btn_reset2.grid(row=5, column=0, pady=(5, 50), padx=120, sticky='sw')

    ## Create an slider space

    master.equalizer_frame.freq3_label = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="125 Hz",
                                            text_font=("Roboto Medium", -12),
                                            fg_color=("white", "gray30"),
                                            width=30)

    master.equalizer_frame.freq3_label.grid(row=2, column=0, pady=(15,0), padx=170, sticky="nw")

    # Slider current value
    master.equalizer_frame.s3_current_value = tk.DoubleVar()

    def slider3_changed(event):
        master.equalizer_frame.s3_value_label.configure(text='{: .2f}'.format(master.equalizer_frame.s3_current_value.get()))

    # Slider
    master.equalizer_frame.slider_3 = ttk.Scale(master.equalizer_frame,
                                from_=0,
                                to=-60,
                                orient=VERTICAL,
                                style="TScale",
                                command=slider3_changed,
                                variable=master.equalizer_frame.s3_current_value)

    master.equalizer_frame.slider_3.grid(row=3, column=0, pady=10, padx=185, sticky="w")

    # Value label
    master.equalizer_frame.s3_value_label = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.equalizer_frame.s3_current_value.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.equalizer_frame.s3_value_label.grid(row=4, column=0, pady=0, padx=181, sticky='sw')

    # Button to reset the slider
    master.equalizer_frame.btn_reset3 = customtkinter.CTkButton(master.equalizer_frame,
                                     text="R",
                                     width=1,
                                     text_font=("Roboto Medium", -9),
                                     height=1,
                                     fg_color="gray40",
                                     command=lambda: f.reset_slider3(master))

    master.equalizer_frame.btn_reset3.grid(row=5, column=0, pady=(5, 50), padx=183, sticky='sw')

    ## Create an slider space

    master.equalizer_frame.freq4_label = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="260 Hz",
                                            text_font=("Roboto Medium", -12),
                                            fg_color=("white", "gray30"),
                                            width=30)

    master.equalizer_frame.freq4_label.grid(row=2, column=0, pady=(15,0), padx=238, sticky="nw")

    # Slider current value
    master.equalizer_frame.s4_current_value = tk.DoubleVar()

    def slider4_changed(event):
        master.equalizer_frame.s4_value_label.configure(text='{: .2f}'.format(master.equalizer_frame.s4_current_value.get()))

    # Slider
    master.equalizer_frame.slider_4 = ttk.Scale(master.equalizer_frame,
                                from_=0,
                                to=-60,
                                orient=VERTICAL,
                                style="TScale",
                                command=slider4_changed,
                                variable=master.equalizer_frame.s4_current_value)

    master.equalizer_frame.slider_4.grid(row=3, column=0, pady=10, padx=250, sticky="w")

    # Value label
    master.equalizer_frame.s4_value_label = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.equalizer_frame.s4_current_value.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.equalizer_frame.s4_value_label.grid(row=4, column=0, pady=0, padx= 246, sticky='sw')

    # Button to reset the slider
    master.equalizer_frame.btn_reset4 = customtkinter.CTkButton(master.equalizer_frame,
                                     text="R",
                                     width=1,
                                     text_font=("Roboto Medium", -9),
                                     height=1,
                                     fg_color="gray40",
                                     command=lambda: f.reset_slider4(master))

    master.equalizer_frame.btn_reset4.grid(row=5, column=0, pady=(5, 50), padx= 247, sticky='sw')

    ## Create an slider space

    master.equalizer_frame.freq5_label = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="500 Hz",
                                            text_font=("Roboto Medium", -12),
                                            fg_color=("white", "gray30"),
                                            width=30)

    master.equalizer_frame.freq5_label.grid(row=2, column=0, pady=(15,0), padx= 305, sticky="nw")

    # Slider current value
    master.equalizer_frame.s5_current_value = tk.DoubleVar()

    def slider5_changed(event):
        master.equalizer_frame.s5_value_label.configure(text='{: .2f}'.format(master.equalizer_frame.s5_current_value.get()))

    # Slider
    master.equalizer_frame.slider_5 = ttk.Scale(master.equalizer_frame,
                                from_=0,
                                to=-60,
                                orient=VERTICAL,
                                style="TScale",
                                command=slider5_changed,
                                variable=master.equalizer_frame.s5_current_value)

    master.equalizer_frame.slider_5.grid(row=3, column=0, pady=10, padx=320, sticky="w")

    # Value label
    master.equalizer_frame.s5_value_label = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.equalizer_frame.s5_current_value.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.equalizer_frame.s5_value_label.grid(row=4, column=0, pady=0, padx=315, sticky='sw')

    # Button to reset the slider
    master.equalizer_frame.btn_reset5 = customtkinter.CTkButton(master.equalizer_frame,
                                     text="R",
                                     width=1,
                                     text_font=("Roboto Medium", -9),
                                     height=1,
                                     fg_color="gray40",
                                     command=lambda: f.reset_slider5(master))

    master.equalizer_frame.btn_reset5.grid(row=5, column=0, pady=(5, 50), padx=317, sticky='sw')


    ## Create an slider space

    master.equalizer_frame.freq6_label = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="1k Hz",
                                            text_font=("Roboto Medium", -12),
                                            fg_color=("white", "gray30"),
                                            width=30)

    master.equalizer_frame.freq6_label.grid(row=2, column=0, pady=(15,0), padx=372, sticky="nw")

    # Slider current value
    master.equalizer_frame.s6_current_value = tk.DoubleVar()

    def slider6_changed(event):
        master.equalizer_frame.s6_value_label.configure(text='{: .2f}'.format(master.equalizer_frame.s6_current_value.get()))

    # Slider
    master.equalizer_frame.slider_6 = ttk.Scale(master.equalizer_frame,
                                from_=0,
                                to=-60,
                                orient=VERTICAL,
                                style="TScale",
                                command=slider6_changed,
                                variable=master.equalizer_frame.s6_current_value)

    master.equalizer_frame.slider_6.grid(row=3, column=0, pady=10, padx=382, sticky="w")

    # Value label
    master.equalizer_frame.s6_value_label = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.equalizer_frame.s6_current_value.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.equalizer_frame.s6_value_label.grid(row=4, column=0, pady=0, padx=378, sticky='sw')

    # Button to reset the slider
    master.equalizer_frame.btn_reset6 = customtkinter.CTkButton(master.equalizer_frame,
                                     text="R",
                                     width=1,
                                     text_font=("Roboto Medium", -9),
                                     height=1,
                                     fg_color="gray40",
                                     command=lambda: f.reset_slider6(master))

    master.equalizer_frame.btn_reset6.grid(row=5, column=0, pady=(5, 50), padx=380, sticky='sw')

    ## Create an slider space

    master.equalizer_frame.freq7_label = customtkinter.CTkLabel(master=master.equalizer_frame,
                                             text="2k Hz",
                                             text_font=("Roboto Medium", -12),
                                             fg_color=("white", "gray30"),
                                             width=30)

    master.equalizer_frame.freq7_label.grid(row=2, column=0, pady=(15,0), padx=430, sticky="nw")

    # Slider current value
    master.equalizer_frame.s7_current_value = tk.DoubleVar()

    def slider7_changed(event):
        master.equalizer_frame.s7_value_label.configure(text='{: .2f}'.format(master.equalizer_frame.s7_current_value.get()))

    # Slider
    master.equalizer_frame.slider_7 = ttk.Scale(master.equalizer_frame,
                                from_=0,
                                to=-60,
                                orient=VERTICAL,
                                style="TScale",
                                command=slider7_changed,
                                variable=master.equalizer_frame.s7_current_value)

    master.equalizer_frame.slider_7.grid(row=3, column=0, pady=10, padx=442, sticky="w")

    # Value label
    master.equalizer_frame.s7_value_label = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.equalizer_frame.s7_current_value.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.equalizer_frame.s7_value_label.grid(row=4, column=0, pady=0, padx=438, sticky='sw')

    # Button to reset the slider
    master.equalizer_frame.btn_reset7 = customtkinter.CTkButton(master.equalizer_frame,
                                     text="R",
                                     width=1,
                                     text_font=("Roboto Medium", -9),
                                     height=1,
                                     fg_color="gray40",
                                     command=lambda: f.reset_slider7(master))

    master.equalizer_frame.btn_reset7.grid(row=5, column=0, pady=(5, 50), padx=440, sticky='sw')

    ## Create an slider space

    master.equalizer_frame.freq8_label = customtkinter.CTkLabel(master=master.equalizer_frame,
                                             text="4k Hz",
                                             text_font=("Roboto Medium", -12),
                                             fg_color=("white", "gray30"),
                                             width=30)

    master.equalizer_frame.freq8_label.grid(row=2, column=0, pady=(15,0), padx=490, sticky="nw")

    # Slider current value
    master.equalizer_frame.s8_current_value = tk.DoubleVar()

    def slider8_changed(event):
        master.equalizer_frame.s8_value_label.configure(text='{: .2f}'.format(master.equalizer_frame.s8_current_value.get()))

    # Slider
    master.equalizer_frame.slider_8 = ttk.Scale(master.equalizer_frame,
                                 from_=0,
                                 to=-60,
                                 orient=VERTICAL,
                                 style="TScale",
                                 command=slider8_changed,
                                 variable=master.equalizer_frame.s8_current_value)

    master.equalizer_frame.slider_8.grid(row=3, column=0, pady=10, padx=500, sticky="w")

    # Value label
    master.equalizer_frame.s8_value_label = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.equalizer_frame.s8_current_value.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.equalizer_frame.s8_value_label.grid(row=4, column=0, pady=0, padx=498, sticky='sw')

    # Button to reset the slider
    master.equalizer_frame.btn_reset8 = customtkinter.CTkButton(master.equalizer_frame,
                                     text="R",
                                     width=1,
                                     text_font=("Roboto Medium", -9),
                                     height=1,
                                     fg_color="gray40",
                                     command=lambda: f.reset_slider8(master))

    master.equalizer_frame.btn_reset8.grid(row=5, column=0, pady=(5, 50), padx=499, sticky='sw')

    ## Create an slider space

    master.equalizer_frame.freq9_label = customtkinter.CTkLabel(master=master.equalizer_frame,
                                             text="8k Hz",
                                             text_font=("Roboto Medium", -12),
                                             fg_color=("white", "gray30"),
                                             width=30)

    master.equalizer_frame.freq9_label.grid(row=2, column=0, pady=(15,0), padx=550, sticky="n")

    # Slider current value
    master.equalizer_frame.s9_current_value = tk.DoubleVar()

    def slider9_changed(event):
        master.equalizer_frame.s9_value_label.configure(text='{: .2f}'.format(master.equalizer_frame.s9_current_value.get()))

    # Slider
    master.equalizer_frame.slider_9 = ttk.Scale(master.equalizer_frame,
                                 from_=0,
                                 to=-60,
                                 orient=VERTICAL,
                                 style="TScale",
                                 command=slider9_changed,
                                 variable=master.equalizer_frame.s9_current_value)

    master.equalizer_frame.slider_9.grid(row=3, column=0, pady=10, padx=562, sticky="w")

    # Value label
    master.equalizer_frame.s9_value_label = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.equalizer_frame.s9_current_value.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.equalizer_frame.s9_value_label.grid(row=4, column=0, pady=0, padx=558, sticky='sw')

    # Button to reset the slider
    master.equalizer_frame.btn_reset9 = customtkinter.CTkButton(master.equalizer_frame,
                                     text="R",
                                     width=1,
                                     text_font=("Roboto Medium", -9),
                                     height=1,
                                     fg_color="gray40",
                                     command=lambda: f.reset_slider9(master))

    master.equalizer_frame.btn_reset9.grid(row=5, column=0, pady=(5, 50), padx=559, sticky='sw')

    ## Create an slider space

    master.equalizer_frame.freq10_label = customtkinter.CTkLabel(master=master.equalizer_frame,
                                             text="16k Hz",
                                             text_font=("Roboto Medium", -12),
                                             fg_color=("white", "gray30"),
                                             width=30)

    master.equalizer_frame.freq10_label.grid(row=2, column=0, pady=(15,0), padx=485, sticky="ne")

    # Slider current value
    master.equalizer_frame.s10_current_value = tk.DoubleVar()

    def slider10_changed(event):
        master.equalizer_frame.s10_value_label.configure(text='{: .2f}'.format(master.equalizer_frame.s10_current_value.get()))

    # Slider
    master.equalizer_frame.slider_10 = ttk.Scale(master.equalizer_frame,
                                 from_=0,
                                 to=-60,
                                 orient=VERTICAL,
                                 style="TScale",
                                 command=slider10_changed,
                                 variable=master.equalizer_frame.s10_current_value)

    master.equalizer_frame.slider_10.grid(row=3, column=0, pady=10, padx=502, sticky="e")

    # Value label
    master.equalizer_frame.s10_value_label = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.equalizer_frame.s10_current_value.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.equalizer_frame.s10_value_label.grid(row=4, column=0, pady=0, padx=502, sticky='se')

    # Button to reset the slider
    master.equalizer_frame.btn_reset10 = customtkinter.CTkButton(master.equalizer_frame,
                                     text="R",
                                     width=1,
                                     text_font=("Roboto Medium", -9),
                                     height=1,
                                     fg_color="gray40",
                                     command=lambda: f.reset_slider10(master))

    master.equalizer_frame.btn_reset10.grid(row=5, column=0, pady=(5, 50), padx=502, sticky='se')


    # Button to browse the input file 1
    master.equalizer_frame.btn_equalize = customtkinter.CTkButton(master.equalizer_frame,
                                                   text="Equalize", width=3,
                                                   command=lambda: f.filtering(master,2),fg_color=("gray75", "gray30"),
                                                   hover_color="#1c94cf",
                                                   border_color="#6a777d",
                                                   border_width=1)
    
    master.equalizer_frame.btn_equalize.grid(row=3, column=0, sticky="ne", padx=(100, 400), pady=0)

    master.equalizer_frame.graphic_label = customtkinter.CTkLabel(master=master.equalizer_frame,
                                          text="Graphical representation:",
                                          text_font=("Roboto Medium", -20),
                                          fg_color=("white", "gray18"),
                                          width=30)  # font name and size in px

    master.equalizer_frame.graphic_label.grid(row=5, column=0, pady=(50, 0), padx=40, sticky="sw")


    plt.rcParams['axes.facecolor'] = '#2e2e2e'

    default_figure = Figure(figsize=(16,9), dpi = 100)
    default_figure.set_facecolor('#2e2e2e')
    ax= default_figure.add_subplot(111)
    ax.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    canvas = FigureCanvasTkAgg(default_figure, master.equalizer_frame)

    canvas.draw()
    canvas.get_tk_widget().configure(background='black', width=300, height=200)
    canvas.get_tk_widget().grid(row=6, column=0, sticky="w", padx=(250, 600), pady=(0,0))

    master.equalizer_frame.no_audio_label = customtkinter.CTkLabel(master=master.equalizer_frame,
                                                                text="No audio loaded",
                                                                text_font=("Roboto Medium", -15),
                                                                fg_color=("white", "gray18"),
                                                                width=30)  # font name and size in px

    master.equalizer_frame.no_audio_label.grid(row=6, column=0, pady=(0, 0), padx=(335,600), sticky="w")

    # Button to save the result
    master.equalizer_frame.save_button = customtkinter.CTkButton(master.equalizer_frame,
                                          text="Save", width=3,
                                          command=lambda: f.save_audio(master.y,44100),
                                          fg_color=("gray75", "gray30"),
                                          state=DISABLED)

    master.equalizer_frame.save_button.grid(row=3, column=0, sticky="e", padx=(100, 410), pady=0)


    #Button to play the result
    master.equalizer_frame.play_result_button = customtkinter.CTkButton(master.equalizer_frame,
                                                 text="▶", width=3,
                                                 command=lambda: f.play_song(master.y, 44100),
                                                 fg_color=("gray75", "gray30"))

    master.equalizer_frame.play_result_button.grid(row=3, column=0, sticky="se", padx=(100, 400), pady=0)

    # Button to stop the result
    master.equalizer_frame.stop_result_button = customtkinter.CTkButton(master.equalizer_frame,
                                                 text="II", width=3,
                                                 command=lambda: f.stop_song(master.y),
                                                 fg_color=("gray75", "gray30"))

    master.equalizer_frame.stop_result_button.grid(row=3, column=0, sticky="se", padx=(100, 440), pady=0)
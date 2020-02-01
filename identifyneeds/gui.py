import tkinter as tk
import logging

from collections import OrderedDict


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class TitlePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        title_text = tk.Label(self, text="Identifying Children's Needs", font=("Arial Bold", 30))
        title_text.pack(side="top")
        credit = tk.Label(self, text="J.Collins 2020", font=("Arial", 10))
        credit.pack(side="bottom")


class TutorialQuestions(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        text_1 = tk.Label(self, text="Answer questions by selecting", font=("Arial Bold", 20))
        text_1.pack(side="top")
        a_lot = tk.Button(self, text="A lot")
        a_lot.pack(side="top")
        a_little = tk.Button(self, text="A little")
        a_little.pack(side="top")
        not_at_all = tk.Button(self, text="Not at all")
        not_at_all.pack(side="top")
        text_2 = tk.Label(self, text="for each one", font=("Arial Bold", 20))
        text_2.pack(side="top")


class TutorialInstructions(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        text_1 = tk.Label(self, text="To change an answer use the back button", font=("Arial Bold", 20))
        text_1.pack(side="top")
        back = tk.Button(self, text="Back")
        back.pack(side="left")
        text_2 = tk.Label(self, text="To move forward again, use the forward button", font=("Arial Bold", 20))
        text_2.pack(side="top")
        next_ = tk.Button(self, text="Next")
        next_.pack(side="right")


class StartPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        text_1 = tk.Button(self, text="Start", font=("Arial Bold", 20))
        text_1.pack(side="right")


class QuestionsOver(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        button_1 = tk.Button(self, text="Change Answers", font=("Arial Bold", 20))
        button_1.pack(side="left")
        button_2 = tk.Button(self, text="See Results", font=("Arial Bold", 20))
        button_2.pack(side="right")


class Results(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        quit_button = tk.Button(self, text="Quit", font=("Arial Bold", 20))
        quit_button.pack(side="right")
        print_button = tk.Button(self, text="Print", font=("Arial Bold", 20))
        print_button.pack(side="left")


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        buttonframe = tk.Frame(self)
        buttonframe.pack(side="bottom", fill="x", expand=True)
        container.pack(side="top", fill="both", expand=True)

        frames_order = [TitlePage, TutorialQuestions, TutorialInstructions, StartPage, QuestionsOver, Results]

        self.frames = OrderedDict()
        for frame_num, frame in enumerate(frames_order):
            page_name = frame.__name__
            frame = frame(container, self)
            self.frames[frame_num] = frame
            logging.info(f"Placing frame: {frame_num}: {page_name} into container")

            frame.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.next_page = tk.Button(buttonframe, text="Next", command=self.next)
        self.next_page.pack(side="right")
        self.previous_page = tk.Button(buttonframe, text="Back", command=self.back)
        self.previous_page.pack(side="left")

        self.current_frame = 0
        self.show_frame(self.current_frame)

    def show_frame(self, frame_num):
        logging.info(f"Showing frame: {frame_num}")
        if frame_num == 0:
            self.previous_page.pack_forget()
        else:
            self.previous_page.pack(side="left")

        if frame_num == list(self.frames.keys())[-1]:
            self.next_page.pack_forget()
        else:
            self.next_page.pack(side="right")

        frame = self.frames[frame_num]
        frame.lift()

    def next(self):
        frame_num_to_try = self.current_frame + 1
        if self.frames.get(frame_num_to_try) is not None:
            self.current_frame = frame_num_to_try
            self.show_frame(frame_num_to_try)
        else:
            logging.info(f"Cannot go forward. Displaying last frame")

    def back(self):
        frame_num_to_try = self.current_frame - 1
        if self.frames.get(frame_num_to_try) is not None:
            self.current_frame = frame_num_to_try
            self.show_frame(frame_num_to_try)
        else:
            logging.info(f"Cannot go back. Displaying first frame.")


if __name__ == '__main__':
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)s - %(levelname)s ] %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)

    # test = QuestionsOver(root)
    # test.pack(side="top", fill="both", expand=True)

    root.title("Identify Needs")
    root.geometry("600x480")
    root.mainloop()

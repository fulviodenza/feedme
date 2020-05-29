import npyscreen

class ExampleTUI(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", myTUI, name="Main TUI Form")

class myTUI(npyscreen.ActionForm):
    def activate(self):
        self.edit()

    def create(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F  = npyscreen.Form(name = "Welcome to Feed-Collector!",)
        argument = F.add(npyscreen.TitleText, name = "Subject you'd like to keep informed:",)
        F.add(npyscreen.TitleSlider, out_of=12, name = "Slider")

        #-------------------------------------------------------------------------------------------

        ms = F.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="Pick One",
                values = ["Option1","Option2","Option3"], scroll_exit=True)
        ms2= F.add(npyscreen.TitleMultiSelect, max_height =-2, value = [1,], name="Pick Several",
                values = ["Option1","Option2","Option3"], scroll_exit=True)

        # This lets the user interact with the Form.
        F.edit()

        print(ms.get_selected_objects())

        def getArgument(self):
            return argument
        

if __name__ == "__main__":
    npyscreen.wrapper(ExampleTUI().run())
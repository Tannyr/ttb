class Menu:
    def __init__(self, title = 'Default Title', options = []):
        self.title = title
        self.options = options
        # menu_title, Options[(key_to_press, option_title, (function to call, *function_arguements))]
        self.acceptable_commands = self.__generate_acceptable_commands()

    def __get_corresponding_command(self, command):
    # return numeric index of command.
        for option in self.options:
            if option[0] == command:
                return option[2]
            
    def display(self):
    # Prints options
        print(self.title)
        for option in self.options:
            print('({}) - {}'.format(option[0], option[1]))
        print ('(q) - Quit')
        
    def __generate_acceptable_commands(self):
    # returns tuple of valid commands
        acceptable_commands = ()
        for option in self.options:
            acceptable_commands += (option[0], )
        return acceptable_commands

    def retrieve_selection(self, command=None):
        command = input('Enter Selection: ')
        while command not in self.acceptable_commands and command != 'q':
            print('Invalid command.')
            command = input('Enter Selection: ')
        if command == 'q':
            return 'q'
        return self.__get_corresponding_command(command)

# Test Functions

def main():
    main.test1 = Menu('Test 1', [('1', 'Test_function 1', test_function2)])
    main.test3 = Menu('Test 3', [('w', 'Test_function 2', test_function4)])
    
    current_menu = main.test1
    
    current_menu.display()
    selection = current_menu.retrieve_selection()
    
    while selection != 'q':
        current_menu = selection()
        current_menu.display()
        selection = current_menu.retrieve_selection()

def test_function2():
    print('yay, passed 1 and executed 2!')
    current_menu = main.test3
    return current_menu


def test_function4():
    print ('passed 3 and executed 4!')
    current_menu = main.test1
    return current_menu


if __name__ == '__main__':
    main()

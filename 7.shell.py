import subprocess

def execute_command(command):
    #Split the command into command and arguments
    command_list = command.split()
    
    #Support IO redirection
    #input from file to process
    input_file = None
    #output from process to file
    output_file = None
    if '<' in command_list:
        input_index = command_list.index('<')
        input_file = command_list[input_index + 1]
        command_list = command_list[:input_index]
    if '>' in command_list:
        output_index = command_list.index('>')
        output_file = command_list[output_index + 1]
        command_list = command_list[:output_index]

    #Shell executes the command with full path to executable
    process = subprocess.Popen(command_list, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
    #e.g. input from one process being output of another
    if input_file:
        with open(input_file, 'r') as f:
            input_data = f.read()
            stdout, stderr = process.communicate(input_data.encode())
    else:
        stdout, stderr = process.communicate()

    #Handle output redirection
    if output_file:
        with open(output_file, 'w') as f:
            f.write(stdout.decode())
    
    return stdout.decode()

#Main shell loop
while True:
    #User inputs command
    user_input = input("Shell> ")
    
    if user_input.lower() == 'exit':
        break
    #Shell prints output
    output = execute_command(user_input)
    print(output)


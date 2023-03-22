from tkinter import *
import customtkinter
import openai
import os
import pickle

# Initiate App
root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry('600x600')
root.iconbitmap('ai.lt.ico') # https://tkinter.com/ai_lt.ico

# Set color scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Submit to ChatGPT
def speak():
	if chat_entry.get():
		# Define our file name
		filename = "api_key"


		try:
			if os.path.isfile(filename):
				# Open the file
				input_file = open(filename, 'rb')

				# Load the data into a variable
				stuff = pickle.load(input_file)

				# Query ChatGPT
				# Define our API key to ChatGPT
				openai.api_key = stuff


					# Create an instance
				openai.Model.list()

					# Define our query response
				response = openai.Completion.create(
					model = "text-davinci-003", 
					prompt = chat_entry.get(),
					temperature = 0,
					max_tokens =60,
					top_p = 1.0,
					frequency_penalty = 0.0,
					presence_penalty=0.0
					)

				my_text.insert(END, (response["choices"][0]["text"]).strip())
				my_text.insert(END, "\n\n")
					
			else:
					# Create the file
				input_file = open(filename, 'wb')
					# Close the file
				input_file.close()
					# Error message - you need an api key
				my_text.insert(END, "\n\nYou need an API key to talk to ChatGPT.Get one here:\nhttps://beta.openai.com/account/api-keys") 


		except Exception as e:
			my_text.insert(END, f"\n\n There was an error\n\n{e}")

	else:
		my_text.insert(END, "\n\nHey, you forgot to type anything!")

# Clear the screens
def clear():
	# Clear the main text box
	my_text.delete(1.0, END)
	# Clear the query entry box
	chat_entry.delete(0, END)

# Do API operations
def key():
	# Define our file name
	filename = "api_key"


	try:
		if os.path.isfile(filename):
			# Open the file
			input_file = open(filename, 'rb')

			# Load the data into a variable
			stuff = pickle.load(input_file)

			# Output to our entry box
			api_entry.insert(END, stuff)
		else:
			# Create the file
			input_file = open(filename, 'wb')
			# Close the file
			input_file.close()

	except Exception as e:
		my_text.insert(END, f"\n\n There was an error\n\n{e}")

	# Resize app larger
	root.geometry('600x750')
	# Show API frame again
	api_frame.pack(pady=30)

# Save the API key
def save_key():
	# Define the filename
	filename = "api_key"

	try:
		# Open file
		output_file = open(filename, 'wb')

		# Add data
		pickle.dump(api_entry.get(), output_file)

		# Delete entry box
		api_entry.delete(0, END)

	except Exception as e:
		my_text.insert(END, f"\n\n There was an error\n\n{e}")

	# Hide API frame
	api_frame.pack_forget()
	# Resize app smaller
	root.geometry('600x600')

# Create text frame
text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)


# Add text widget to get ChatGPT responses
my_text = Text(text_frame, 
	bg="#343638",
	width=65,
	bd=1,
	fg="#d6d6d6",
	relief="flat",
	wrap=WORD,
	selectbackground="#1f538d")
my_text.grid(row=0, column=0)

# Create scrollbar for text widget
text_scroll = customtkinter.CTkScrollbar(text_frame, command=my_text.yview)
text_scroll.grid(row=0, column=1, sticky="ns")

# Add the scrollbar to the textbox
my_text.configure(yscrollcommand=text_scroll.set)

# Entry widget to talk to ChatGPT
chat_entry = customtkinter.CTkEntry(root,
	placeholder_text="Ask ChatGPT...",
	width=535,
	height=50,
	border_width=1)
chat_entry.pack(pady=10)

# Create button frame
button_frame = customtkinter.CTkFrame(root, fg_color="#242424")
button_frame.pack(pady=10)


# Create Submit button
submit_button = customtkinter.CTkButton(button_frame, 
	text="Talk to ChatGPT", 
	command=speak)
submit_button.grid(row=0, column=0, padx=25)

# Create Clear button
clear_button = customtkinter.CTkButton(button_frame, 
	text="Clear response", 
	command=clear)
clear_button.grid(row=0, column=1, padx=35)

# Create API button
api_button = customtkinter.CTkButton(button_frame, 
	text="Update API key", 
	command=key)
api_button.grid(row=0, column=2, padx=25)

# Add API key frame
api_frame = customtkinter.CTkFrame(root, border_width=1)
api_frame.pack(pady=30)

# Add API entry widget
api_entry = customtkinter.CTkEntry(api_frame,
	placeholder_text="Enter your API key",
	width=350, height=50, border_width=1)
api_entry.grid(row=0, column=0, padx=20, pady=20)

# Add API button
api_save_button = customtkinter.CTkButton(api_frame,
	text="Save key", 
	command=save_key)
api_save_button.grid(row=0, column=1, padx=10)


root.mainloop()


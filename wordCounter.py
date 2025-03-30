
from pynput.keyboard import Key, Listener
from win10toast import ToastNotifier

# Initialize the ToastNotifier object
toaster = ToastNotifier()
keys = []
word_count_session = 0
word_count = 1000  # Total word count across different sessions
target_word_count = 1000  # Replace with your desired target word count

def on_press(key):
    global word_count_session, keys
    if key == Key.space:
        word_count_session += 1
    elif key == Key.esc:
        return False
    keys.append(key)
    write_file(keys)
    if word_count_session >= 1000:
        session_info()

def session_info():
    global word_count, word_count_session
    word_count += word_count_session
    word_count_session = 0
    if word_count > target_word_count:
        # Notification Message
        message = f"Congrats! You have achieved your {target_word_count} Words Daily Target"
        toaster.show_toast("Counter ⏱️", message, duration=10)

def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            if key == Key.space:
                f.write(' ')
            else:
                k = str(key).replace("'", "")
                if k[0:3] == 'Key':
                    pass
                else:
                    f.write(k)

with Listener(on_press=on_press) as listener:
    listener.join()

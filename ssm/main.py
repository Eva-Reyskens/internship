def split_into_paragraphs(text):
    """Split text into paragraphs based on 'content_copy user-img' and 'chatbot-img' delimiters."""
    user_text = []
    chatbot_text = []
    current_user = None

    for line in text.strip().split('\n'):
        if line.startswith('user-img'):
            current_user = 'user'
            user_text.append(line[len('content_copy user-img'):].strip())
        elif line.startswith('chatbot-img'):
            current_user = 'chatbot'
            chatbot_text.append(line[len('chatbot-img'):].strip())
        elif current_user == 'user':
            user_text[-1] += ' ' + line.strip()
        elif current_user == 'chatbot':
            chatbot_text[-1] += ' ' + line.strip()

    return user_text, chatbot_text


def analyze_text(paragraphs):
    """Analyze paragraphs and calculate total statistics."""
    total_words = 0
    total_chars_with_spaces = 0
    total_chars_no_spaces = 0

    for para in paragraphs:
        word_count = len(para.split())
        chars_with_spaces = len(para)
        chars_no_spaces = len(para.replace(" ", ""))

        total_words += word_count
        total_chars_with_spaces += chars_with_spaces
        total_chars_no_spaces += chars_no_spaces

    return total_words, total_chars_with_spaces, total_chars_no_spaces


def paragraph_stats(paragraph):
    """Calculate statistics for a given paragraph."""
    word_count = len(paragraph.split())
    chars_with_spaces = len(paragraph)
    chars_no_spaces = len(paragraph.replace(" ", ""))
    return word_count, chars_with_spaces, chars_no_spaces


def shortest_paragraph(paragraphs):
    """Find the shortest paragraph based on word count."""
    if not paragraphs:
        return None
    shortest = min(paragraphs, key=lambda para: len(para.split()))
    return shortest, paragraph_stats(shortest)


def longest_paragraph(paragraphs):
    """Find the longest paragraph based on word count."""
    if not paragraphs:
        return None
    longest = max(paragraphs, key=lambda para: len(para.split()))
    return longest, paragraph_stats(longest)


def analyze_conversation(text):
    """Analyze conversation between two persons."""
    user_text, chatbot_text = split_into_paragraphs(text)

    user_totals = analyze_text(user_text)
    chatbot_totals = analyze_text(chatbot_text)


    print("\nUser Total Statistics:")
    print("-" * 50)
    print(f"Total Words: {user_totals[0]}")
    print(f"Total Characters (with spaces): {user_totals[1]}")
    print(f"Total Characters (without spaces): {user_totals[2]}")

    print("\nChatbot Total Statistics:")
    print("-" * 50)
    print(f"Total Words: {chatbot_totals[0]}")
    print(f"Total Characters (with spaces): {chatbot_totals[1]}")
    print(f"Total Characters (without spaces): {chatbot_totals[2]}")

    # Shortest and longest paragraphs - user
    shortest_user_result = shortest_paragraph(user_text)
    if shortest_user_result:
        shortest_user_para, shortest_user_stats = shortest_user_result
        print("\nShortest User Paragraph:")
        print(shortest_user_para)
        print(
            f"Words: {shortest_user_stats[0]}, Characters (with spaces): {shortest_user_stats[1]}, Characters (without spaces): {shortest_user_stats[2]}"
        )
    else:
        print("\nNo user paragraphs found for shortest paragraph analysis.")

    longest_user_result = longest_paragraph(user_text)
    if longest_user_result:
        longest_user_para, longest_user_stats = longest_user_result
        print("\nLongest User Paragraph:")
        print(longest_user_para)
        print(
            f"Words: {longest_user_stats[0]}, Characters (with spaces): {longest_user_stats[1]}, Characters (without spaces): {longest_user_stats[2]}"
        )
    else:
        print("\nNo user paragraphs found for longest paragraph analysis.")

    # Shortest and longest paragraphs - chatbot
    shortest_chatbot_result = shortest_paragraph(chatbot_text)
    if shortest_chatbot_result:
        shortest_chatbot_para, shortest_chatbot_stats = shortest_chatbot_result
        print("\nShortest Chatbot Paragraph:")
        print(shortest_chatbot_para)
        print(
            f"Words: {shortest_chatbot_stats[0]}, Characters (with spaces): {shortest_chatbot_stats[1]}, Characters (without spaces): {shortest_chatbot_stats[2]}"
        )
    else:
        print("\nNo chatbot paragraphs found for shortest paragraph analysis.")

    longest_chatbot_result = longest_paragraph(chatbot_text)
    if longest_chatbot_result:
        longest_chatbot_para, longest_chatbot_stats = longest_chatbot_result
        print("\nLongest Chatbot Paragraph:")
        print(longest_chatbot_para)
        print(
            f"Words: {longest_chatbot_stats[0]}, Characters (with spaces): {longest_chatbot_stats[1]}, Characters (without spaces): {longest_chatbot_stats[2]}"
        )
    else:
        print("\nNo chatbot paragraphs found for longest paragraph analysis.")

# Example text - replace this with your actual text
sample_text = """
user-img
Hi! What was stolen from the party?

chatbot-img
Based on the clues I have, there are two valuable items that could have been stolen: Mrs. Klutz's expensive diamond ring and the Hosts' painting by Artisimisso. I can confirm that Ms. Perceptive noticed that a picture she had admired was not there when she left the party, suggesting the painting might have been stolen.

user-img
Was Mr.Klutz briefcase empty when he arrived?

chatbot-img
I don't have any clues about Mr. Klutz's briefcase or its contents when he arrived at the party. However, I do know that Mr. Klutz is a dealer in fine art and needed money badly to keep his business from failing.


"""

analyze_conversation(sample_text)


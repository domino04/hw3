def extract_info(note_list):

    result = []

    for note in note_list:
        title = note.find("a", {"class" : "N=a:bta.title"}).string
        img_src = note.find("img")["src"]
        page_link = note.find("div", {"class" : "thumb_type thumb_type2"}).find("a")["href"]
        writer = note.find("a", {"class" : "txt_name N=a:bta.author"}).string
        cop = note.find("a", {"class" : "N=a:bta.publisher"}).string
        note_info = {
            'title' : title,
            'img_src' : img_src,
            'page_link' : page_link,
            'writer' : writer,
            'cop' : cop
        }
        result.append(note_info)

    return result

    print(result)

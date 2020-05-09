def extract_info(hospital_list):

    final_result = []

    for note in hospital_list:
        tds = note.contents

        note_info = {
            '시도' : tds[1].string,
            '시군구' : tds[2].string,
            '선별진료소' : tds[3].text,
            '전화번호' : tds[4].string
        }
        final_result.append(note_info)

    return final_result

    print(final_result)
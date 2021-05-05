import re, remove_stopwords

def combining_words(output):
    for i in range(len(output)):
        if output[i]=='as' :
            try:
                if (output[i+1] == 'needed'):
                    output[i] = 'as needed'
                    output[i+1] = ''
                if (output[i+1] == 'applicable'):
                    output[i] = 'as applicable'
                    output[i+1] = ''
            except:
                pass
        if (output[i]=='from') :
            try:
                if (output[i+1] == 'time'):
                    if (output[i+2] == 'to'):
                        if (output[i+3] == 'time'):
                            output[i] = 'from time to time'
                            output[i+1] = ''
                            output[i+2] = ''
                            output[i+3] = ''
            except:
                pass
        if (output[i] == 'otherwise'):
            try:
                if (output[i+1] == 'reasonably'):
                    output[i] = 'otherwise reasonably'
                    output[i+1] = ''
            except:
                pass
        if (output[i]=='among') :
            try:
                if (output[i+1] == 'other'):
                    if (output[i+2] == 'things'):
                        output[i] = 'among other things'
                        output[i+1] = ''
                        output[i+2] = ''
            except:
                pass
        if (output[i]=='including') :
            try:
                if (output[i+1] == 'but'):
                    if (output[i+2] == 'not'):
                        if (output[i+3] == 'limited'):
                            if (output[i+4] == "to"):
                                output[i] = 'including but not limited to'
                                output[i+1] = ''
                                output[i+2] = ''
                                output[i+3] = ''
                                output[i+4] = ''
            except:
                pass
    while True:
        try:
            output.remove('')
        except:
            break            
    return output

def preprocess_text(txt_input):
    output = txt_input.lower()
    output = re.sub(r'[^a-z0-9 ]','' ,output)
    output = output.split()
    output = combining_words(output)
    return output

def generate_distrubution(list_input):
    nonstopword_count = remove_stopwords.count_without_stopwords(list_input)
    Condition = ['depending', 'necessary', 'appropriate',
                 'inappropriate', 'as needed', 'as applicable',
                 'otherwise reasonably', 'sometimes',
                 'from time to time']
    Generalization = ['generally', 'mostly', 'widely',
                      'general', 'commonly',
                      'usually', 'normally', 'typically',
                      'largely', 'often', 'primarily',
                      'among other things']
    Modality = ['may', 'might', 'can', 'could', 'would',
                'likely', 'possible', 'possibly']
    Numeric_quantifier = ['anyone', 'certain', 'everyone',
                          'numerous', 'some', 'most', 'few',
                          'much', 'many', 'various', 
                          'including but not limited to']
    cond_count, gen_count, mod_count, num_counter, vague_words = 0,0,0,0,0
    for i in list_input:
        if i in Condition:
            cond_count += 1
            vague_words += 1
        if i in Generalization:
            gen_count += 1
            vague_words += 1
        if i in Modality:
            mod_count += 1
            vague_words += 1
        if i in Numeric_quantifier:
            num_counter += 1
            vague_words += 1
    if vague_words == 0:
        return (0,0,0,0,0, nonstopword_count)
    percent = (cond_count*100/vague_words, gen_count*100/vague_words,
               mod_count*100/vague_words, num_counter*100/vague_words,
                vague_words, nonstopword_count )
    return percent
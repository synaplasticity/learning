

def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    print('Document id\'s used : ', strlist)
    file = open('stories_small.txt')

    lines_list = list(file)

    index_lines_list = [(document_id, line) for (document_id, line) in list(enumerate(lines_list)) if document_id in strlist] 
    print('Enumerated lines list size : ' +  str(len(index_lines_list)))


    _words_set = set()
    for(id, line) in index_lines_list:
        _words_set.update(set(line.split()))


    print ('Words size : ' + str(len(_words_set)))

    _inverse_index_dict = dict()
    for word in _words_set:
        _document_id_set = set()

        _document_id_set.update({doc_id for (doc_id, line) in index_lines_list if word in line})
        _inverse_index_dict[word] = _document_id_set

    
    return _inverse_index_dict

def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """

    print ("Query : ", query)

    _document_id_set = set()
    for word in query:
    	_document_id_set.update(inverseIndex[word] if word in inverseIndex else ())

    return _document_id_set

 ## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    print ("Query : ", query)

    _document_id_set = set()
    for word in query:
    	if _document_id_set == set():
    		_document_id_set.update(inverseIndex[word] if word in inverseIndex else {})
    	else:
    		_document_id_set.intersection_update(inverseIndex[word] if word in inverseIndex else {})

    return _document_id_set
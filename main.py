import sys
import os
import fs

from xml.etree import ElementTree as ET

#init global variables
xliff_translated_result = []
source_language, target_language = '',''

#Find all trans-units with target state=needs-translation from input .xlf file
def findTransFromSource(filename: str):
    #Create tree from .xlf File //TODO: dateinput variabel gestalten
    if filename != '':
        tree = ET.parse(filename)
        root = tree.getroot()

    
    for file in root.iter():
        if file.tag == '{urn:oasis:names:tc:xliff:document:1.2}file':
            source_language = file.get('source-language')
            target_language = file.get('target-language')
        elif file.tag == '{urn:oasis:names:tc:xliff:document:1.2}group' :
            #group ebene
            if file.get('id') == 'body':
                #trans-unit ebene
                for trans_unit in file.findall('{urn:oasis:names:tc:xliff:document:1.2}trans-unit'):
                    target = trans_unit.find('{urn:oasis:names:tc:xliff:document:1.2}target')
                    if target is not None:
                        #Wenn target state= translated, sichere übersetzung
                        dev_translation, xliff_generated_reference = '',''
                        if target.get('state') == 'translated':
                            for note in trans_unit.findall('{urn:oasis:names:tc:xliff:document:1.2}note'):
                                if note.get('from') == 'Developer':
                                    dev_translation = note.text
                                elif note.get('from') == 'Xliff Generator':
                                    xliff_generated_reference = note.text
                        if (dev_translation != '') and (xliff_generated_reference != ''):
                            if (target_language != '') and (source_language != ''):
                                if (source_language in dev_translation) or (target_language in dev_translation):
                                    xliff_translated_result.append([xliff_generated_reference, dev_translation])
    #return result alphabetically sorted
    return(sorted(xliff_translated_result))

#find file name for translation results
def findFileForTransResult(list_to_sort: list):
    sorted_trans_list = []
    for element in list_to_sort:
        file_to_extend = element[0].split(' -')[0]
        rest_of_file_to_extend = element[0].split('- ')[1] + ' ' + element[1]    
        sorted_trans_list.append([file_to_extend, rest_of_file_to_extend])
    return(sorted_trans_list)





#call defined funcitons
kekw = findFileForTransResult(findTransFromSource('country_data.xlf'))

print(kekw)
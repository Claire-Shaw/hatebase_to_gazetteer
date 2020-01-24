import hatebase_extract
import write_gazetteer

path = '/home/claclab/Documents/Claire/python_scripts/hatebase/get_vocabulary'
output_file = 'hatebase_eng.lst'

# See docs for extraction parameter options
# https://github.com/hatebase/Hatebase-API-Docs/blob/master/current/v4-4/get_vocabulary.md
extract_params = {'language': 'ENG'}

# See docs for field options and descriptions 
# https://github.com/hatebase/Hatebase-API-Docs/blob/master/current/v4-4/get_vocabulary.md
fields_to_write = ['is_unambiguous',
                   'average_offensiveness',
                   'plural_of',
                   'variant_of',
                   'transliteration_of',
                   'is_about_nationality',
                   'is_about_ethnicity',
                   'is_about_religion',
                   'is_about_gender',
                   'is_about_sexual_orientation',
                   'is_about_disability',
                   'is_about_class',
                   'hateful_meaning']

if __name__ == "__main__":
    #hatebase_extract.get_vocabulary(path, extract_params)
    write_gazetteer.write(path, fields_to_write, output_file)
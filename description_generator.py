import os
# import openai
from core.terrains.forest import Forest
from core.terrains.field import Field
from core.terrains.village import Village
from core.terrains.graveyard import Graveyard

template = 'Дай короткое художественно описание пейзажа - '


def generate_field_description(token):

    list_of_localities = [Field, Village, Forest, Graveyard]

    for localy in list_of_localities:
        title = localy._title
        for seed in localy._seed_list:
            st = f'{seed} {title}'
            new_st = template + st + '.'

            # response = openai.Completion.create(
            #     engine="text-davinci-002",
            #     prompt=new_st,
            #     max_tokens=100,
            #     api_key=token,
            # )
            # text = response['choices'][0]['text']
            text = new_st

            with open(f'fields_description/{st}.txt', 'w') as file:
                file.write(text)

            file.close()

    print('end')


if __name__ == '__main__':
    token = os.environ.get('CHATGPT_TOKEN')

    if token:
        generate_field_description(token)

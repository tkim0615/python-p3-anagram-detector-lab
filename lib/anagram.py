import ipdb
class Anagram:
    def __init__(self, word):
        self.word = sorted(word)

    def match(self, input_list):
        match_list = []
        for word in input_list:
            sorted_word = sorted(word)
            if sorted_word== self.word:
                match_list.append(word)
        return match_list
    # 인풋 리스트에 단어가 3개라면, 포룹이 시작되고 첫번째 단어가 소트되고 그 단어가 이닛에서 받은 소트된 단어와 같은지 첵하고
    # 동일하면  매치리스트 리스트에 넣음. 나머지 2개 단어도 반복함. if 문이 포룹 안에 잇어야함. 밖에 있으면 포룹이 3번 다 돌고
    #이프문이 실행되기때문에 각 단어를 체크하지 않음. 3번 다 실행하고 끝나면 리턴해야함. 그래서 리턴문은 밖에 있음.

        

hello = Anagram('hello')
print(hello.match(['llohe', 'hi']))

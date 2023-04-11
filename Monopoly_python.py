#TeamProj_SUNMOON-MARBLE
######################################
#'''MODULES'''
######################################
import random as rd

######################################
#'''CLASSES'''
######################################
# 플레이어 클래스
class Player:
    '''플레이어 정보 :
    __init__(self, number, name, order = None, wallet = 100_000, position = 0, wealth = 0)'''
    
    def __init__(self, number, name, wallet, order = None, position = 0, wealth = 0):   
        self.number = number #플레이어 초기화 순서
        self.name = name #플레이어 이름
        self.wallet = wallet #지갑
        self.order = order #주사위 순서
        self.position = position #위치
        self.wealth = wealth #전재산 지갑 + 건물가격 + 땅가격
        self.own_maps = [] # 소유지의 인덱스
        
        self.island_turn = 0 #무인도 대기 턴
        
    def __str__(self):
        return '"{}" 정보 :: 주사위 순서 : {} | 지갑: {}원 | 현재위치: {} | 전재산: {}원 | 소유한 맵: {}'\
    .format(self.name, self.order, self.wallet, self.position, self.wealth, self.own_maps)
    
    def set_wealth(self):
        '''플레이어의 전재산을 (재)설정하기 위한 함수. '''
        # 지갑 더하기
        self.wealth = self.wallet
        # 맵에 지불한 값 더하기
        for c_map in map_class.values():
            # 플레이어가 소유자인 땅일 경우
            if c_map.owner == self.name:
                # 건물이 지어져 있는 경우
                if c_map.is_building == True:
                    self.wealth += c_map.price + c_map.building_price
                # 건물이 안 지어져 있는 경우
                else:
                    self.wealth += c_map.price
        
    
class Map:
    '''맵 정보:
    __init__(self, index, name, map_price, map_building_price): '''
    def __init__(self, index, name, map_price, map_building_price):
        self.index = index # 맵 순서
        self.name = name # 맵 이름
        self.price = map_price # 맵 가격
        self.building_price = map_building_price # 맵 빌딩 가격
        self.passage_cost = 0 # 맵 통행료
        self.owner = 'None' # 맵 소유자
        self.is_building = False # 맵에 건물이 지어졌는가

    def set_map_passage_cost(self):
        '''현재 땅(플레이어 위치)의 통행료를 지정함. INT'''
        #만약 건물이 있을 경우
        if self.is_building == True:
            self.passage_cost = round((self.price + self.building_price / 2) * 1.15)
        else:
            self.passage_cost = round((self.price / 2) * 1.15)

        

######################################
# PRINT_RETURN_FUNCTIONS
######################################

def print_line():
    '''--------------------------을 출력함.'''
    print('-'*110)
    
def print_d_line():
    '''==========================을 출력함.'''
    print('='*110)

def return_player_name():
    '''현재 플레이어 턴의 플레이어 이름을 반환함. STRING'''
    return player_class[now_player_turn].name

def return_player_position():
    '''현재 플레이어 턴의 플레이어 위치값(int)을 반환함. INT'''
    return player_class[now_player_turn].position

def return_player_wallet(player = None):
    '''현재 플레이어 턴의 플레이어 지갑(남은 돈)을 반환함. INT
        인자 개수 : 1. -> 플레이어 이름 입력하면 그 플레이어의 지갑상황을 알려줌.'''
    if player:
        for i, c_player in player_class.items():
            if player == c_player.name: #입력된 이름 = 플레이어 객체의 이름
                return player_class[i].wallet #지갑
    else:
        return player_class[now_player_turn].wallet

def return_player_wealth():
    '''현재 플레이어의 전재산을 반환함. INT'''
    return player_class[now_player_turn].wealth
    
def return_player_own_maps():
    '''현재 플레이어가 소유한 땅의 index를 반환함. LIST(INT)'''
    return player_class[now_player_turn].own_maps
    
def return_map_index():
    '''현재 플레이어가 있는 곳의 건물 번호를 반환함. INT'''
    return map_class[return_player_position()].index
    
def return_map_name():
    '''현재 플레이어가 있는 곳의 건물 이름을 반환함. STRING'''
    return map_class[return_player_position()].name

def return_map_price():
    '''현재 플레이어 턴의 플레이어가 있는 위치의 땅값을 반환함. INT'''
    return map_class[return_player_position()].price

def return_map_building_price():
    '''맵 건물 건설 가격을 반환함. INT'''
    return map_class[return_player_position()].building_price

def return_map_owner_name():
    '''None 이나, 이 땅의 소유자를 반환함. STRING'''
    return map_class[return_player_position()].owner
    
def return_map_is_building():
    '''맵 건물이 건설되었는지 알려줌. BOOL'''
    return map_class[return_player_position()].is_building

def return_map_passage_cost():
    '''현재 플레이어가 있는 땅 통행세 가격을 반환함. INT'''
    return map_class[return_player_position()].passage_cost
    
def set_map_building():
    '''땅에 건물이 지어졌다고 선언 예) False -> True. BOOL'''
    map_class[return_player_position()].is_building = True
    
def set_map_owner(player):
    '''현재 플레이어가 있는 맵 소유자 player로 정함. 예) None -> player
    다른 플레이어의 소유지로 지정하고 싶으면 인수 입력.'''
    if player:
        map_class[return_player_position()].owner = player

    else: map_class[return_player_position()].owner = return_player_name()

    
def print_map_info(length = 0):
    '''맵 정보를 출력. 아무런 인자를 받지 않을 경우 맵 전체를 출력. 인자 받을 시, 인자의 수 만큼 플레이어 앞 맵의 정보를 출력.'''
    if length:
        print_line(); print('플레이어 현재 위치 : {} - {}\n플레이어 앞 6칸 맵 정보 : '.format(return_player_position(), return_map_name()))
        print_line(); print('{:>4}  |  {:^34} |{:^5}| {:^5}|{:^6}| {:^7} | {:^10}'.format('번호', '이름', '땅가격', '건물가격', '건물여부', '소유자', '통행료')); print_line()

        for i in range(length): #length 만큼 플레이어 앞의 맵 정보를 출력.
            i += 1
            index = i + return_player_position()
            if index > 23:
                index = index % len(map_names)
                c_map = map_class[index]
            else:
                c_map = map_class[index]
            print('{:>7} | {:<25}   \t| {:>6} |{:>9} | {:^9}| {:^10} | {:>10}\n'.format(c_map.index, c_map.name, c_map.price, c_map.building_price, c_map.is_building, c_map.owner, c_map.passage_cost))
        print('\n')
    else:
        print_line(); print('맵 정보 : ')
        print_line(); print('{:>4}  |  {:^34} |{:^5}| {:^5}|{:^6}| {:^7} | {:^10}'.format('번호', '이름', '땅가격', '건물가격', '건물여부', '소유자', '통행료'));print_line()

        for c_map in map_class.values():
            print('{:>7} | {:<25}   \t| {:>6} |{:>9} | {:^9}| {:^10} | {:>10}\n'.format(c_map.index, c_map.name, c_map.price, c_map.building_price, c_map.is_building, c_map.owner, c_map.passage_cost))
        

######################################
# EVENT FUNCTIONS
######################################

def rd_dice():
    '''주사위 굴리기 : 1~ 6까지의 수. INT'''
    dice = rd.randint(1, 6)
    return dice

def buy_map_building():
    '''buy_map_building 함수 기능 :  도착한 땅이,
                                                        1) 소유자 없을 시 땅 구매, 
                                                        2) 소유지일 경우 건물 건설,
                                                        3) 타유지일 경우 통행료 지불'''

    global now_player_turn, map_class, player_class
    # 땅의 소유자가 없을 경우
    if return_map_owner_name() == 'None':
        print('사유지가 아닙니다.')
        print('{}의 가격은 {}원입니다.'.format(return_map_name(), return_map_price()))
        print('{}님의 지갑사정은 현재 {}원 입니다.'.format(return_player_name(), return_player_wallet()))
        #돈이 부족할 경우
        if return_player_wallet() < return_map_price(): 
            print('돈이 없군요. 가던 길 가세요.')
        #돈이 충분하다면
        else:
            # 땅 구매 시스템 시작
            while True:
                user_answer = input('땅을 구매하실 건가요(y/n)? ')
                if user_answer in 'yYnN' and user_answer != '':
                    if user_answer in 'yY':
                        player_class[now_player_turn].wallet -= return_map_price()
                        print('{}님이 땅을 구매했습니다.'.format(return_player_name()))      
                        print('{}님의 지갑사정은 현재 {}원 입니다.'.format(return_player_name(), return_player_wallet()))

                        set_map_owner(return_player_name()) # 땅 소유자 -> player로 변경.
                        map_class[return_player_position()].set_map_passage_cost() # 통행료 매기기(재설정)

                        print('{}은(는) 이제부터 {}님의 소유지입니다.'.format(return_map_name(), return_map_owner_name()))
                        return_player_own_maps().append(return_map_index())
                        break

                    else:
                        print('{}님이 땅 구매를 취소했습니다.'.format(return_player_name()))
                        break
                else:
                    print('다시 입력하세요.')

    #땅의 소유자가 있을 경우
    else:
        print('{}은 {}의 사유지입니다.'.format(return_map_name(), return_map_owner_name()))
        # 나의 땅이 아닌 경우
        if  return_player_name() != return_map_owner_name():
            print('{}님이 {}님에게 통행료를 지불했습니다.'.format(return_player_name(), return_map_owner_name()))
            #이렇게 표현할 수 있음. 아래로 플레이어 정보 리스트의 값을 변경시키기 위해 아래처럼 풀어씀.
            owner_name = return_map_owner_name()

            for i, c_player in player_class.items():
                if owner_name == c_player.name:
                    owner_id = i # 소유자의 number를 찾았다!

                    # 소유지에 도착한 플레이어 : 의 지갑 -(통행료)-> 땅의 소유자 플레이어 : 의 지갑
                    # 지갑의 돈이 부족하다 -> 파산 시스템으로 이동
                    if return_player_wallet() < return_map_passage_cost():
                            go_broke(return_map_passage_cost())
                            player_class[owner_id].wallet += return_map_passage_cost() #사유지 소유자는 돈을 받고
                    # 돈이 통행료를 낼 만큼 충분하다
                    else:
                        print('\n', '플레이어 현금이동'.center(30,'-'))
                        print('{}:{} -({})-> {}:{}'.format(return_player_name(), return_player_wallet(), return_map_passage_cost(),\
                                                    return_map_owner_name(), return_player_wallet(return_map_owner_name())))
                        player_class[owner_id].wallet += return_map_passage_cost() #사유지 소유자는 돈을 받고
                        player_class[now_player_turn].wallet -= return_map_passage_cost() # 통행자는 통행료를 내고
                        print('현재 {}의 지갑엔 {}원이 남았습니다.'.format(return_player_name(), return_player_wallet()))
                    #ID찾고, 나머지 필요없는 연산 중지.
                    break

        #도착한 땅이 내 사유지일 경우
        else:
            print('통행료는 없습니다.')
            # 건물이 안지어져 있는 경우
            if return_map_is_building() == False:
                # 지갑 형편 체크
                if return_player_wallet() >= return_map_building_price():
                    while True:
                        user_answer = input('건물을 지으시겠습니까?(y/n): ')
                        # 입력 문자 필터링
                        if user_answer in 'yYnN' and user_answer != '':
                            if user_answer in 'yY':
                                player_class[now_player_turn].wallet -= return_map_building_price() # 건물 건설 비용 지출
                                map_class[return_player_position()].is_building = True # 건물 건설됨 선언
                                map_class[return_player_position()].set_map_passage_cost() # 건물 가격 포함한 통행료 매기기
                                print('건물 건설완료. 변경된 통행료 : {}원'.format(return_map_passage_cost()))
                                break
                            else:
                                print('건물 건설을 취소합니다.')
                                break
                        else:
                            print('다시입력하세요.')
                #건물을 지을 돈이 없는 경우
                else:
                    print('건물을 건설할 비용이 부족합니다.')
            #건물이 지어져 있는 경우
            else:
                print('건물이 이미 지어져 있습니다.')


def get_income():
    '''현재 턴의 플레이어에게 월급 주는 함수.'''
    global income, now_player_turn
    player_class[now_player_turn].wallet += income
    print('{}에게 월급 {}원이 들어왔습니다. {} 지갑:{}'.format(return_player_name(), income, return_player_name(), return_player_wallet()))
    
def turn_end():
    '''턴 종료를 알리는 함수. 현재 턴과 플레이어 정보 출력, 각 플레이어 전재산 변환, 전재산에 따라 순위 지정.
    만약, 파산 안한 플레이어가 한 명일 경우 = 게임 종료.'''

    global player_class, turn, is_finish_game
    # 플레이어가 혼자 남았을 경우 = 게임 종료
    player_list = []
    for c_player in player_class.values():
        if c_player.wallet != None:
            player_list.append(c_player.name)
    # 혼자 남았을 경우
    if len(player_list) == 1:
        is_finish_game = True

    # 2명 이상 남았을 경우
    else:
        print_line(); print('< {}턴 종료 >'.format(turn)); print_line()
        print('현재 플레이어 정보 :'); print_line()

        player_info_list = []

        for c_player in player_class.values():
            if c_player.wallet == None:
                continue
            else:
                c_player.set_wealth()
                player_info_list.append(c_player)
                player_info_list = sorted(player_info_list, key = lambda x: x.wealth, reverse = True) # 전재산으로 순위를 지정

        print('{:^4} | {:^12}  | {:^5} | {:^10} | {:^15}'.format('순위', '이름', '현재위치', '지갑', '총재산'))
        print_line()
        for i, info in enumerate(player_info_list, start = 1):
            print('{:>6} | {:^15} |  {:>8} | {:>12} | {:>15}\n'.format(i, info.name, info.position, info.wallet, info.wealth))
        print_d_line()

def go_broke(you_need):
    '''파산 기능 실현 함수. 현재 플레이어 정보 파기. -> 지갑 None으로 지정. but, 자신의 땅을 팔아서 돈을 얻을 수 있음.'''
    global now_player_turn, map_class
    #지갑 내 충분히 돈이 있다.
    if return_player_wallet() >= you_need:
        player_class[now_player_turn].wallet -= you_need
        print('현재 {}님의 지갑: {}원'.format(return_player_name(), return_player_wallet())); print_d_line()
    #돈이 부족
    else:
        print('{}님의 지갑 속 현금이 부족합니다.'.format(return_player_name()))
        #플레이어 전재산이 you_need 보다 크거나 같을 경우
        if return_player_wealth() >= you_need:
            # 플레이어 지갑에 필요한 돈이 충분히 없을 경우
            while return_player_wallet() < you_need:
                #플레이어가 소유한 맵 표시
                print_line()
                print('필요한 현금 : {}원\n현재 {}님의 지갑 : {}원'.format(you_need, return_player_name(), return_player_wallet()))
                print_line(); print('{:>4}  |  {:^34} |{:^7}| {:^5}| {:^10}'.format('번호', '이름', '판매시 받는 가격', '건물여부', '통행료')); print_line()
                for c_map in map_class.values():
                    if c_map.index in return_player_own_maps():
                        if c_map.is_building == True: # 건물이 지어진 판매가
                            print('{:>7} | {:<25}   \t| {:>15} |{:>10} | {:>10}\n'.format(c_map.index, c_map.name, c_map.price + c_map.building_price, c_map.is_building, c_map.passage_cost)); print('\n')
                        else: # 건물이 없는 판매가
                            print('{:>7} | {:<25}   \t| {:>15} |{:>10} | {:>10}\n'.format(c_map.index, c_map.name, c_map.price, c_map.is_building, c_map.passage_cost));                      
                # 판매할 땅 숫자 입력
                sell_map = input('판매할 땅을 고르세요(위 표에 있는 땅 숫자 입력, 땅 판매 종료 = q): ')
                if sell_map in 'qQ':
                    while True:
                        quit_input = input('이대로 종료하면 파산됩니다. 종료하실 겁니까?(y/n): ')
                        if quit_input in 'yYnN' and quit_input != '':
                            # 파산
                            if quit_input in 'yY':
                                print('소유한 땅 판매를 종료합니다.')
                                # 파산처리
                                for c_map in map_class.values():
                                    if c_map.index in return_player_own_maps(): #소유자 이름과 지금 파산하는 이름과 같을 경우 -> None으로 모두 변환한다.
                                        map_class[c_map.index].owner = 'None' # 맵 소유자 이름 제거
                                        map_class[c_map.index].is_building = False # 건물 지어진 것 모두 철거
                                        map_class[c_map.index].passage_cost = 0 # 통행세 제거
                                        player_class[now_player_turn].own_maps.remove(c_map.index) # 플레이어 변수에서 제거

                                player_class[now_player_turn].wallet = None # 지갑 = None으로 파산 판정.
                                player_class[now_player_turn].own_maps = [] # 현재 플레이어 own_maps 초기화
                                print_d_line(); print('\n{}님이 파산하였습니다.\n'.format(return_player_name())); print_d_line()
                                break
                            # 다시 땅 판매로 회귀
                            else:
                                print('다시 땅 판매 시스템으로 전환합니다.')
                        # 입력 필터링
                        else:
                            print('다시 입력하세요.')
                    break
                elif sell_map.isdigit() == False:
                    print('다시 입력하세요.')
                # 지정한 맵 판매
                else:
                    sell_map = int(sell_map)
                    if sell_map not in return_player_own_maps():
                        print('다시 입력하세요.')
                    #숫자입력이 올바른 경우
                    else:
                        print('"{} - {}"을 판매하셨습니다.'.format(map_class[sell_map].index, map_class[sell_map].name))
                        # 판매 후 받는 금액 = 맵 땅 가격 + (건물이 지어져 있을 경우)맵 건물 가격
                        if map_class[sell_map].is_building:
                            player_class[now_player_turn].wallet += map_class[sell_map].price + map_class[sell_map].building_price
                        else:
                            player_class[now_player_turn].wallet += map_class[sell_map].price
                        # 플레이어 객체의 맵 소유 변수에서 판매한 맵 제거
                        player_class[now_player_turn].own_maps.remove(map_class[sell_map].index)
                        #맵 데이터 삭제 : 소유자, 건물여부, 통행료
                        map_class[sell_map].owner, map_class[sell_map].is_building, map_class[sell_map].passage_cost = 'None', False, 0

            print('내야할 돈을 다 지불했습니다.')
            print('현재 {}님의 지갑: {}원'.format(return_player_name(), return_player_wallet())); print_d_line()

        #플레이어 전재산이 you_need 보다 작을 경우
        else:
            # 1. 이 플레이어가 지닌 소유자 명 제거하기( 통행세도 제거), 2. 이 플레이어 지갑 None으로 처리
            for c_map in map_class.values():
                if c_map.index in return_player_own_maps(): #소유자 이름과 지금 파산하는 이름과 같을 경우 -> None으로 모두 변환한다.
                    map_class[c_map.index].owner = 'None' # 소유자 이름 제거
                    map_class[c_map.index].is_building = 'False' #  건물 지어진 것 모두 철거
                    map_class[c_map.index].passage_cost = 0 # 통행세 제거

            player_class[now_player_turn].own_maps = [] #플레이어 소유 땅 초기화
            player_class[now_player_turn].wallet = None # 지갑 = None으로 파산 판정.
            print_d_line(); print('\n{}님이 파산하였습니다.\n'.format(return_player_name())); print_d_line()

def is_float(number):
    '''실수인지 아닌지 확인하는 함수. BOOL'''
    if '.' in number:
        if number.split('.')[0].isdigit() and number.split('.')[1].isdigit():
                return True
        else:
            return False
    else:
        return False

def in_special_maps(position):
    '''시작, 기숙사, 콜벤, 학생회 감사, 국민은행 도착 후 일어나는 이벤트 발생 함수.'''
    global now_player_turn, fine_wallet
    
    if position == 0: #시작지점 도착
        # 플레이어의 소유지가 없는 경우
        if return_player_own_maps() == False:
            print('소유한 땅이 없네요.')
            print('건물 건설을 중지합니다.')
        # 플레이어의 소유지가 있다
        else:
            # 돈 확인
            lower_price = 50_000 # 그냥 특정값을 기준으로 정함.

            c_maps_player_own = [c_map for c_map in map_class.values() if c_map.index in return_player_own_maps()]
            # 건물이 안지어진 맵 필터링
            c_is_building_false_maps = [] # 건물 안지어진 땅 리스트

            for c_map in c_maps_player_own:
                # 맵의 건물가격이 lower_price보다 낮을 경우
                if c_map.is_building == False: # 건물이 안지어진 맵
                    c_is_building_false_maps.append(c_map)
                    
                    if c_map.building_price < lower_price:
                        lower_price = c_map.building_price # 가장 낮은 가격 얻기

            # 건물이 안지어진 맵이 없는 경우
            if c_is_building_false_maps == False:
                print('건물이 안지어진 소유지가 없네요.')
                print('건물 건설을 중지합니다.')
            # 건물이 안지어진 맵이 존재
            else:
                # 가장 낮은 가격보다 현금이 적을 경우
                if lower_price > return_player_wallet():
                    print('돈이 부족하네요. 건물 건설을 취소합니다.')
                # 플레이어 건물건설 시작
                else:
                    while True:
                        # 땅의 건물이 모두 지어진 경우
                        if c_is_building_false_maps == False:
                            print('{}님의 모든 소유지에 건물이 건설되어 있네요.'.format(return_player_name()))
                            print('건물 건설을 중지합니다.')
                            break

                        # 플레이어 맵 목록 불러오기
                        print_line(); print('{}님의 지갑 : {}원\n{}님의 건물이 지어지지 않은 맵 : '.format(return_player_name(), return_player_wallet(), return_player_name()))
                        print_line(); print('{:>4}  |  {:^34} |{:^5}| {:^5}|{:^6}| {:^7}'.format('번호', '이름', '땅가격', '건물가격', '건물여부', '통행료'));print_line()
                        # 플레이어가 지닌 땅을 찾기 + 건물이 지어지지 않은 맵
                        for c_map in c_is_building_false_maps:
                            print('{:>7} | {:<25}   \t| {:>6} |{:>9} | {:^9}| {:>10}\n'.format(c_map.index, c_map.name, c_map.price, c_map.building_price, c_map.is_building, c_map.passage_cost))
                        map_index = input('건물을 건설할 맵의 번호를 입력하세요(취소 = q): ')
                        # 입력 조건
                        if map_index.isdigit() == False: # STRING 필터링
                            # 건물 건설 취소
                            if map_index in 'qQ' and map_index != '':
                                print('건물 건설을 취소합니다.')
                                break
                            else: # 잘못된 STRING
                                print('다시 입력하세요.')
                        # 정상적으로 입력됨
                        elif int(map_index) in [c_map.index for c_map in c_is_building_false_maps]:
                            selected_map = map_class[int(map_index)]
                            #돈이 부족한 경우
                            if return_player_wallet() < selected_map.building_price:
                                print('돈이 부족합니다.')
                            #돈이 충분한 경우
                            else:
                                print('{}원을 지불하고, 건물을 건설했습니다.'.format(selected_map.building_price))
                                c_is_building_false_maps.remove(selected_map) #지금 건물 지은 맵을 건물X 리스트에서 재거
                                player_class[now_player_turn].wallet -= selected_map.building_price # 플레이어 지출
                                selected_map.is_building = True # 건물 건설 선언
                                map_class[selected_map.index].set_map_passage_cost() # 건물가격을 포함한 통행료로 변경
                                break
                        else:
                            print('다시 입력하세요.')
        
    elif position == 6: #무인도 도착
        if player_class[now_player_turn].island_turn == 0: #처음 도착
            player_class[now_player_turn].island_turn = max_island_turn
            print('기숙사에 도착했으므로 {}턴 간 자가격리해야 합니다.'.format(max_island_turn))
        else: #처음 도착한 게 아니다.
            print('{} 턴 쉬셔야 합니다.'.format(player_class[now_player_turn].island_turn))
            player_class[now_player_turn].island_turn -= 1

    elif position == 12: #학생회 감사하는 곳
        print('학생회 감사를 시작합니다. 감사원 지갑에 들어갈 벌금 {}원 납부하십시오.'.format(fine))
        if return_player_wallet() < fine:
            go_broke(fine)

        else: #벌금 낼 돈이 있음.
            print('벌금 {}원을 지불했습니다.'.format(fine))
            print('{}:{} -({})-> {}:{}'.format(return_player_name(), return_player_wallet(), fine, '학교 통장', fine_wallet))
            player_class[now_player_turn].wallet -= fine
            print('현재 지갑에 {}원이 남아있습니다.'.format(return_player_wallet()))
            fine_wallet += fine
            print('현재 학교 통장에 {}원이 남아있습니다.'.format(fine_wallet))


    elif position == 18: # 콜벤에 도착.
        if callben_cost > return_player_wallet(): #콜벤 탈 돈이 없다.
                print('콜벤 탈 돈이 없으시네요. 여기서 머물다가 자기 턴 돌아오면 나가세요.')
    
        else: #콜벤 탈 돈이 있다.
            while True:
                print_map_info()
                callben_move_count = input('원하는 곳으로 이동할 수 있습니다.\n이동할 장소의 번호를 입력하시오.(0~{}) :'\
                    .format(len(map_class.values())-1))
                if callben_move_count.isdigit() == False or callben_move_count == '': #잘못 입력됐을 경우
                    print('숫자만 입력하시오.')
                elif int(callben_move_count) == 18:
                    print('이미 여기가 18번 맵입니다. 다시 입력하세요.')
                elif int(callben_move_count) not in map_class.keys():
                    print('0 ~ 23 사이의 숫자를 입력하시오.')
                else: # 정상적으로 입력됨
                    callben_move_count = int(callben_move_count) # int화
                    #지금 위치(18)에서 뒤쪽(17)으로 이동하는 경우엔, 한바퀴를 지나서 왔다는 경우를 적용함.
                    while return_player_position() != callben_move_count:
                        player_class[now_player_turn].position += 1
                        if return_player_position() % 24 == 0: #시작을 지났을 때 월급주기, 지금 장소에서 / 24로 올바른 위치값으로 변환.
                            get_income()
                            player_class[now_player_turn].position = 0
                    # 콜벤타고 도착한 곳에서 땅구매, 건물구매, 통행료 지불
                    # 특별 맵에 도착할 경우
                    if return_player_position() in special_maps_index:
                        in_special_maps(return_player_position())
                        break
                    # 일반 맵에 도착한 경우
                    else:
                        buy_map_building()
                        break


    elif position == 22: #국민은행 도착 - 감사원에게ㅐ서 장학금 받음 id == 22
        print('현재 학교 통장에 {}원이 있습니다.'.format(fine_wallet))
        if fine_wallet == 0:
            print('학교에서 줄 장학금이 없습니다.')

        else: #돈이 있을 경우
            print('장학금 {}원을 받았습니다.'.format(fine_wallet))
            player_class[now_player_turn].wallet += fine_wallet
            fine_wallet = 0



#####################################
# 프로그램 시작
#####################################

#게임 규칙 변수 기본값
max_player = 4 # 최대 플레이어 수
turn = 0 # 현재 턴
max_turn = 15 #최대 턴
passage_incerease_per_turn = 5 # 통행료 증가 턴
passage_incerease = 1.5 # 통행료 증가 턴 마다 증가하는 통행료 퍼센트
income = 20_000 # 월급
start_money = 100_000 # 시작 금액
callben_cost = 10_000 # 콜벤 가격
fine = 10_000 # 학생회 감사에 도착 시 내는 벌금
max_island_turn = 2 # 무인도 대기 최대 턴

fine_wallet = 0 # 감사원 지갑

is_finish_game = False #특정 경우로 인해 게임이 종료되어야 하는 경우 == True
stop = False # 프로그램 완전 종료용 변수

special_maps_index = [0, 6, 12, 18, 22] # 특별 이벤트 맵 인덱스 리스트

while stop == False:
    print('\n\n◇◆◇◆◇◆◇◆ <◁◀ 선 문 마 블 ▶▷> ◆◇◆◇◆◇◆◇\n')
    print('1. 게임 시작\n\n2. 게임종료'); print('\n\n')
    user_input = input('입력 : ')
    # 입력 필터링
    if user_input.isdigit() == False or user_input == '' or user_input not in ['1', '3']:
        print('다시 입력하세요.')
    # 정상입력
    else:
        #게임종료
        if user_input == 2: print('게임을 종료합니다.'); break

        #게임시작
        else:
            print_line(); print('< 게임 규칙 >'); print_line()
            print('주사위 한 개(1~6)를 던져서 주사위 수 만큼 플레이어가 각 맵에 도착해서 땅을 구입함.')
            print('다른 플레이어가 자신의 맵에 도착하면 통행료를 지불.')
            print('{}턴이 지날때마다 각 맵 통행료 {}% 상승'.format(passage_incerease_per_turn, int((passage_incerease - 1) *100)))
            print('기숙사(6)에 도착하면, {}턴 간 휴식.'.format(max_island_turn))
            print('학생회 감사(12)에 도착하면 {}원 벌금 지불.'.format(fine))
            print('콜벤(18)에 도착하면, {}원 지불 후 원하는 곳으로 이동.'.format(callben_cost))
            print('국민은행(22)에 도착하면 학생회 감사에서 지불된 벌금을 장학금으로 받게 됨.')
            print('\n')
            print_line(); print('< 승리 조건 >'); print_line()
            print('1) 마지막 턴에서 전재산이 가장 많은 플레이어가 승리.')
            print('2) 나머지 플레이어들을 모두 파산시키고, 혼자 남은 플레이어가 승리.')
            print('\n')
            print('< 아무거나 입력하세요 >'.center(30, '=')); input()
            #플레이어 수 입력받기
            while True:
                player_count = input('몇 명의 플레이어가 참여하나요?(2~{}): '.format(max_player)) #플레이어 수 입력

                #플레이어 수 확인 : 4명 이상, 2명 미만의 플레이어는 참여할 수 없습니다.
                if player_count.isdigit() == False:
                    print('!) 2 ~ {} 까지의 숫자를 입력하시오.\n'.format(max_player))

                elif int(player_count) > 4 or int(player_count) < 2:
                    print('!) {}명 초과, 1명 이하의 플레이어는 참여할 수 없습니다.\n'.format(max_player))

                else: #게임 플레이 시작
                    player_count = int(player_count)
                    break


            #플레이어 클래스 메모리 주소를 담은 딕셔너리 생성: player_class
            temp_player_info = list()
            for i in range(player_count):
                i += 1

                while True: #플레이어 이름 정하기
                    player_name = input('플레이어{}의 이름을 입력하시오(최대 글자 수 : 10) : '.format(i))
                    #플레이어 이름 오류 필터링
                    if player_name == '': print('공백은 안됩니다. 다시 입력하세요.') #플레이어 이름이 공백일 경우 
                    elif len(player_name) > 10: print('글자 수가 10을 초과했습니다. 다시 입력하세요.') #10글자 초과 시
                    elif player_name.isdigit() == True: print('플레이어 이름에 숫자만 입력 불가능합니다.')# 이름이 숫자일 경우
                    else: # 플레이어 이름이 정상일 경우
                        player = Player(i, player_name, start_money)
                        temp_player_info.append(player)
                        break

            #주사위 던지는 순서가 담긴 리스트 생성
            player_dice_order = []
            ran_num = rd.randint(1,player_count)

            for i in range(player_count):
                while ran_num in player_dice_order: 
                    ran_num = rd.randint(1,player_count)

                player_dice_order.append(ran_num) #랜덤으로 [1, 2, 3, 4]

            # 주사위 던지는 순서 랜덤으로 지정된 값, 순서에 맞게 플레이어 클래스에 각각 부여
            for i in range(player_count):
                order = player_dice_order[i]
                temp_player_info[i].order = order
 
            # 랜덤으로 선정된 순서에 맞게 플레이 시작.
            player_class = dict(enumerate(sorted(temp_player_info, key = lambda c_player: c_player.order), start = 1))
            # 플레이어 순서 출력
            print_line(); print('< 플레이어 주사위 순서 >'); print_line()
            print(' {:^30} | {:^3}'.format('플레이어 이름', '순서')); print_line()
            for c_player in player_class.values():
                print('{:^34} \t| {:<3}'.format(c_player.name, c_player.order))
            
            print(' < 아무거나 입력하세요 > '.center(30, '=')); input()

            #맵 만들기
            map_names = ['시작', '동아리연습실', '학생회관', '중앙도서관', '글로컬산학협력관', '오렌지식당', '기숙사(코로나 격리)'\
                        , '산학협력관', '체육관', '스포츠과학관', '운동장', '공학관', '학생회 감사(벌금)', '아메리카나', '코나킹'\
                        , '본관', '자연과학관', '인문관', '콜벤', '축구장', '보건의료관', '학군단', '국민은행(장학금)', '원화관']
            map_prices = [0, 1_000, 4_000, 5_000, 3_000, 2_000, 0, 10_000, 15_000, 17_000, 13_000, 19_000, fine, 20_000, 25_000, 30_000, 28_000, 27_000, 0, 33_000, 35_000, 31_000, 0, 50_000]
            map_owners = ['None' for i in range(len(map_names))] #맵 소유자 초기화
            map_building_prices = [0] * len(map_names)
            for index, price in enumerate(map_prices):
                map_building_prices[index] = int(price * 1.5) # 맵 건물 가격 = 맵 가격 * 1.5

            map_class = dict() # 맵 클래스 딕셔너리
            
            for i in range(len(map_names)):
                c_map = Map(i, map_names[i], map_prices[i], map_building_prices[i])
                map_class[i] = c_map

            #특정 맵의 경우, 가격과 소유자를 '-'로 표시.
            for i, c_map in map_class.items():
                if i in special_maps_index:
                    c_map.price, c_map.building_price, c_map.owner, c_map.passage_cost = '-', '-', '-', '-'
                    if i == 12: # 단, {12 : 학생회 감사}는 {통행료 == 벌금}으로 지정.
                        c_map.passage_cost = fine

            print_map_info() #전체 맵 정보 출력

    ###########################
    #'''Turn START'''
    ###########################
            #1턴 부터 마지막 15턴까지 알고리즘
            while turn < max_turn:
                turn += 1 # 1턴으로 시작.

                if turn % passage_incerease_per_turn == 0: # 5턴마다 통행료 상승
                    for c_map in map_class.values():
                        if c_map.passage_cost == '-':
                            continue
                        #학생회 감사 땅 통행료(벌금) 상승 금지
                        elif c_map.index == 12:
                            continue
                        c_map.passage_cost = round(c_map.passage_cost * passage_incerease)
                        
                for i in range(player_count): #플레이어 수 만큼, 반복
                    i += 1
                    now_player_turn = i

                    print('\n< 현재 플레이어 차례는 {}입니다. >'.format(return_player_name()))    

                    if return_player_wallet() == None: #이 플레이어는 파산됨.
                        print('{}는 파산했으므로 턴을 종료합니다.'.format(return_player_name()))

                    else: # 이 플레이어는 파산하지 않음.
                        #현재 플레이어 위치가 무인도가 아닌경우
                        if player_class[now_player_turn].island_turn == 0:
                            print_map_info(6) # 현재 플레이어 위치 앞 6칸을 출력.
                            print(' <주사위 굴리기 (아무거나 입력하시오.)> '.center(30, '='))
                            input() # 아무거나 입력하기 위한 input
                            # 주사위를 던졌다!
                            player_dice = rd_dice() 
                            player_class[now_player_turn].position += player_dice
                            print('"{}"칸 이동\n'.format(player_dice))

                            # 이동하다가 맵을 한 바퀴 돌았을 경우 월급 지급.
                            if player_class[now_player_turn].position >= len(map_class):
                                #플레이어의 위치값이 맵 길이(24)를 넘겼을 경우. 맵 길이만큼 나눠서 플레이어 위치 반환.
                                player_class[now_player_turn].position = return_player_position() % len(map_class)
                                #월급 부여
                                get_income()

                            print('""{}"은 {}에 도착하였습니다.\n'.format(return_player_name(), return_map_name()))


                            #특정맵에 도착하지 않았을 경우
                            if return_player_position() not in special_maps_index:
                                # 땅 구매할 건가 = 함수
                                buy_map_building()
                    

                            else: # 특정 맵에 도착함.
                                in_special_maps(return_player_position())
                        
                        else:
                            in_special_maps(return_player_position())

                turn_end() #턴 종료. 현황 알리기
                
                # 마지막 턴이 끝남 or 승리 조건 달성 시 게임 종료
                if is_finish_game == True or turn == max_turn:
                    print('\n' * 2); print('< 모든 턴 종료 >'); print('\n')
                    
                    player_info_list = []
                    for c_player in player_class.values():
                        # 파산한 사람은 게임 결과에서 제외
                        if c_player.wallet == None:
                            continue
                        player_info_list.append(c_player)
                        
                        
                    final_player_info_list = sorted(player_info_list, key = lambda x: x.wealth, reverse = True) # 전재산으로 순위를 지정

                    print('{:^4} | {:^12}  | {:^5} | {:^10} | {:^15}'.format('순위', '이름', '현재위치', '지갑', '총재산'))
                    print_line()
                    for i, info in enumerate(final_player_info_list, start = 1):
                        print('{:>6} | {:^15} |  {:>8} | {:>12} | {:>15}\n'.format(i, info.name, info.position, info.wallet, info.wealth))
                    print('\n'*2); print('게임이 종료되었습니다.'); print('프로그램을 종료합니다.')
                    print_d_line()
                    # 프로그램 종료
                    stop = True
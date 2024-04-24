# Տրված է երկու բնական թիվ. Պարզեք, թե դրանցից որն ունի թվանշանների ավելի մեծ գումար:
# (Սահմանել ֆունկցիա բնական թվի թվանշանների գումարը հաշվարկելու համար):

def num_digit_sum(number):
    digit_sum = 0
    for digit in str(number):
        digit_sum += int(digit)
    return digit_sum


def compare_digits_sum(num1, num2):
    sum1 = num_digit_sum(num1)
    sum2 = num_digit_sum(num2)
    if sum1 > sum2:
        return num1
    elif sum1 < sum2:
        return num2
    else:
        return "Summarys of digits are equal."


# Ստացեք բոլոր վեցանիշ երջանիկ թվերը: Վեցանիշ թիվը կոչվում է երջանիկ, եթե առաջին երեք նիշերի գումարը հավասար է նրա
# վերջին երեք թվանշանների գումարին: (Սահմանեք ֆունկցիա՝ որը կվերադարձնի թիվը երջանիկ է թէ չէ)

def lucky_num_check(num):
    num = str(num)
    first_half_sum = 0
    second_half_sum = 0
    for i in range(int(len(num) / 2)):
        first_half_sum += int(num[i])
    for j in range(int(len(num) / 2), len(num)):
        second_half_sum += int(num[j])
    return first_half_sum == second_half_sum


# Տրված է նախադասություն որը իր մեջ պարունակում է l տառը. Գտե՛ք, թե որ նախադասություն մեջ տրված տառը ավելի մեծ
# հերթական համար ունի (նախադասության սկզբից հաշվելիս): Եթե նախադասության մեջ կան մի քանի a տառեր, ապա պետք է հաշվի առնել
# նրանցից վերջինը. (Սահմանե՛ք ֆունկցիա՝ նախադասության մեջ որոշակի տառի վերջին հայտնված տառի հերթական համարը գտնելու համար):

def find_letter_pos(letter, sentence):
    return sentence.rfind(letter)


# Պատկերացրեք, որ տաքսի ծառայությունից օգտվելու գումարը բաղկացած է
# բազային ուղեվարձից՝ $4,00 գումարած $0,25 140 մետր ճանապարհորդության համար:
# Գրեք ֆունկցիա, որն ընդունում է որպես իր միակ պարամետր
# ճանապարհորդության հեռավորությունը կիլոմետրերով և վերադարձնում է վճարման ընդհանուր գումարը։
# Հիմնական ծրագիրը պետք է ցույց տա արդյունքը։

def get_trip_cost(distance):
    trip_len = (distance * 1000) / 140
    trip_cost = trip_len * 0.25 + 4
    return trip_cost


def main(distance):
    print(f"$ {get_trip_cost(distance)}")


# Գրեք ֆունկցիա որը պետք է ստանա որպես պարամետր զանգված, և բուլյան տիպի փոփոխական
# Ֆունկցիան պետք է սորտավորի տվյալ զանգվածը աճման և նվազման կարգով ըստ փոխանցված բուլյան արժեքի,գրել ֆունկցիան
# չօգտագործելով սորտավորման համար ներդրված ֆունկցիաները
# 5 2 7 1 2
def sort_nums(num_list, reverse=False):
    count = 0
    if not reverse:
        for i in num_list:
            for j in num_list:
                if i > j:
                    count += 1
            num_list.insert(count,num_list.index(i))
            count = 0
        return num_list

print(sort_nums([5, 4, 6, 1, 2]))


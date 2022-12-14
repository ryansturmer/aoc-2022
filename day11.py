import sys, os
import itertools
import input
import copy

'''
 Starting items: 83, 88, 96, 79, 86, 88, 70
  Operation: new = old * 5
  Test: divisible by 11
    If true: throw to monkey 2
    If false: throw to monkey 3
'''

def main():
    part1 = None
    part2 = None
    monkeys = {}
    for monkey in list(input.all.split('\n\n')):
        line = monkey.split('\n')
        num = int(line[0].split()[-1].strip(':'))
        lines = monkey.split('\n')
        items = list(map(int, line[1].split(':')[1].split(',')))
        operation = line[2].split('=')[-1].strip()
        a,op,b = operation.split()
        div = int(line[3].split()[-1])
        true = int(line[4].split()[-1])
        false = int(line[5].split()[-1])
        monkeys[num] = {
            'items' : items,
            'a' : a,    
            'b' : b,
            'op' : op,
            'div' : div,
            'true' : true,
            'false' : false,
            'inspections' : 0
        }

    def play_round(monkeys, worry_mitigator=None):
        monkeys = copy.deepcopy(monkeys)
        for mid in sorted(monkeys.keys()):
            monkey  = monkeys[mid]
            print("Monkey %d" % mid)
            print("   Items: %s" % monkey['items'])
            while monkey['items']:
                item = monkey['items'].pop(0)     
                print('Inspecting %d' % item)
                monkey['inspections'] += 1
                a = item if monkey['a'] == 'old' else int(monkey['a']) 
                b = item if monkey['b'] == 'old' else int(monkey['b'])
                match monkey['op'].strip():
                    case '*':                    
                        worry_level = a*b
                    case '+':
                        worry_level = a+b
                    case '-':
                        worry_level = a-b
                    case '/':
                        worry_level = a/b

                print('  Worry level = %d %s %d : %d' % (a, monkey['op'], b, worry_level))
                worry_mitigator = worry_mitigator or (lambda x : x // 3)
                worry_level = worry_mitigator(worry_level)
                print('  Worry level reduced to %d' % worry_level)

                if worry_level % monkey['div'] == 0:
                    print('  Worry level divisible by %d' % monkey['div'])
                    print('  Throwing %d to %d' % (worry_level, monkey['true']))
                    monkeys[monkey['true']]['items'].append(worry_level)
                else:
                    print('  Worry level not divisible by %d' % monkey['div'])
                    print('Throwing %d to %d' % (worry_level, monkey['false']))
                    monkeys[monkey['false']]['items'].append(worry_level)

        return monkeys

    og_monkeys = monkeys
    factor = 1
    for mid, monkey in og_monkeys.items():
        factor *= monkey['div']

    monkeys = og_monkeys
    for i in range(20):
        monkeys = play_round(monkeys, worry_mitigator = lambda x :x // 3)
        
    print('After round %d' % (i+1))
    for mid in sorted(monkeys.keys()):
        print('Monkey %d inspected items %d times' % (mid, monkeys[mid]['inspections']))
    print('\n\n')

    inspections = [monkeys[id]['inspections'] for id in sorted(monkeys.keys())]
    ranked_inspections = sorted(inspections)
    monkey_business = ranked_inspections[-1]*ranked_inspections[-2]
    part1 = monkey_business

    monkeys = og_monkeys
    for i in range(10000):
        monkeys = play_round(monkeys, worry_mitigator = lambda x :x % factor)

    inspections = [monkeys[id]['inspections'] for id in sorted(monkeys.keys())]
    ranked_inspections = sorted(inspections)
    monkey_business = ranked_inspections[-1]*ranked_inspections[-2]
    part2 = monkey_business

    return (part1, part2)

if __name__ == '__main__':
    part1, part2 = main()
    print('-----------------------')
    print('    Advent of Code')
    print('-----------------------')
    print('')
    print('Part 1 Solution:')
    print(part1)

    print('\n')
    print('Part 2 Solution:')
    print(part2)
    print('')

import re
import sys
import operator

"""
Create this graph by starting with in and replacing any labels with the actualy subgraphs
{
  s<1351:{
    a<2006:{
      x<1416: ***A***
      {
        x>2662:***A***
        ***R***
      }
    }
    m>2090:***A***
    {
      s<537:{
        a>3333:***R***
        ***R***
      }
      x>2440:***R***
      ***A***
    }
  }
  s>2770:{
    s>3448:***A***
    {
      m>1548:***A***
      ***A***
    }
  }
  m<1801:{
    m>838:***A***
    {
      a>1716:***R***
      ***A***
    }
  }
  ***R***
}
Paths that lead to an ***A*** are added to total
 s < 1351
   a < 2006
     x < 1416 -> A
     x > 2662 -> A
   m > 2090 -> A
   s < 537
     a > 3333
For instance going into s<1351 and a<2006 and x<1416 is the first path to being approved.
So the values s = [1, 1350] && a [1, 2005] && x [1, 1415] which is 1351*2006*1416*4000 possibilities: 3,834,799,990
The next path is s<1351 and a<2006 and x>2662 which is 1351*2006*1338*4000 possibilities: 3,626,121,828
s<1351 and m > 2090 -> 
"""

def calculate(graph, part):
    cur = 'in'
    while cur not in 'AR':
        broken = False
        for w in graph[cur][:-1]:
            vertex, op, ch, number = w
            opx = operator.lt if op == '<' else operator.gt
            value = part['xmas'.find(ch)]
            if opx(value, number):
                cur = vertex
                broken = True
                break
        if not broken:
            cur = graph[cur][-1]
    return cur

def main():
    L = [x.strip() for x in sys.stdin]
    D = []

    graph = {}

    y = 0
    for y, line in enumerate(L):
        if line.startswith("{"):
            xmas = []
            for m in re.finditer(r'\d+', line):
                xmas.append(int(m[0]))
            D.append(xmas)
        elif line:
            name = line.split("{")[0]
            rest = line.split("{")[1][:-1]
            graph[name] = []
            for p in rest.split(","):
                vertex = p
                condition = lambda x: True
                if p.find(":") != -1:
                    vertex = p.split(":")[1]
                    left = p.split(":")[0]
                    ch = left[0]
                    number = int(left[2:])
                    op = left[1]
                    graph[name].append((vertex, op, ch, number))
                else:
                    graph[name].append(vertex)

    p1 = 0
    print(graph)
    for d in D:
        print(d)
        final = calculate(graph, d)
        if final == 'A':
            p1 += sum(d)

    print('Part 1:', p1)

if __name__ == '__main__':
    main()

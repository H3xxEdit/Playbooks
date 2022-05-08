import os
import subprocess
import sys
import io

from pyflowchart import *

def input():
    print('input')


def output(fc):
    print('in output')
    file1 = io.open("out_new.txt", "w", newline='\n')
    file1.write(fc.flowchart())
    file1.close()
    subprocess.Popen(['diagrams', 'flowchart', 'out_new.txt', 'flowchart5.svg'], stdout=None, stderr=None, shell=True)
    #subprocess.run(['diagrams flowchart out_new.txt flowchart5.svg'], shell=True)
    #subprocess.Popen(['echo','"Hello World!"'],stdout=None, stderr=None,shell=True)
    #subprocess.Popen(['cmd','diagrams flowchart out_new.txt flowchart3.svg'],stdout=None, stderr=None,shell=True)
    #os.popen('diagrams flowchart out_new.txt flowchart3.svg')

def start():
    st = StartNode("a pyflow test:>http://www.google.com")
    op = OperationNode('do something')
    cond = ConditionNode('Yes or No?')
    io = InputOutputNode(InputOutputNode.OUTPUT, 'something...')
    sub = SubroutineNode('A Subroutine')
    e = EndNode('a_pyflow_test')

    st.connect(op)
    op.connect(cond)
    cond.connect_yes(io)
    cond.connect_no(sub)
    sub.connect(op, "right")  # sub->op line starts from the right of sub
    io.connect(e)

    fc = Flowchart(st)
    print(fc.flowchart())
    output(fc)


def start1():
    file1 = open("out_new.txt", "w" , encoding='utf-8')
    st1 = ['st0=>start: start a_pyflowtest:>http://www.google.com', 'op1=>operation: do something', 'cond2=>condition: Yes or No?', 'io3=>inputoutput: output: something...', 'e5=>end: end a_pyflow_test', 'sub4=>subroutine: A Subroutine', 'st0->op1', 'op1->cond2', 'cond2->', 'cond2->', 'cond2(yes)->io3', 'io3->e5', 'cond2(no)->sub4', 'sub4(right)->op1']
    for line in st1:
        file1.write(line)
        file1.write('\r')
    #file1.write(st1)
    file1.close()

if __name__ == '__main__':

    start()
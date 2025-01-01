import matplotlib.pyplot as mp
def create_expression_png(equation):
    mp.figure(figsize=(6,3), facecolor='white')
    mp.axis('off')
    mp.text(1,1, equation, horizontalalignment='center', verticalalignment='center', fontsize=22)

    mp.savefig('expression.png', bbox_inches='tight', pad_inches=0.2)
    mp.close()
create_expression_png("3 + 8")
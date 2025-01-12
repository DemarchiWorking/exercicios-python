from flask import Flask, render_template_string
import random
import io
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)

def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Recuperando a LCS
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_str.reverse()  # A sequência está de trás para frente, então invertemos
    return dp[m][n], ''.join(lcs_str)

@app.route('/')
def plot():
    X = "AGGTAB"
    Y = "GXTXAYB"
    length_lcs, lcs_str = lcs(X, Y)
    print(f"Comprimento da LCS: {length_lcs}")
    print(f"Sequência LCS: {lcs_str}")

    html = f"""
    <h1>Problema da Sequência Longa Comum (LCS)</h1>
    <p>String X: {X}</p>
    <p>String Y: {Y}</p>
    <p>Comprimento da LCS: {length_lcs}</p>
    <p>Sequência LCS: {lcs_str}</p>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)

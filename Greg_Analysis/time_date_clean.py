import numpy as np

#usuage examples with accident dataframe "df"

# df = df.loc[is_str(df.Time.values),:]  (this would get rid of any None in a string feature. get_hour won't work with Nones)

# df[['y','m','d']] = get_ymd(df.Date.values)
# df['h'] = get_hour(df.Time.values)


def is_str(x):
    Nx = len(x)
    I = np.ones(Nx).astype(bool)
    for ii in range(Nx):
        if type(x[ii]) != str:
            I[ii] = False
    return I

def get_hour(T):
    Nt = len(T)
    H = np.zeros(Nt).astype(int)
    for ii in range(Nt):
        s = T[ii].split(':')
        h = int(s[0])
        m = int(s[1])
        if m > 30:
            h += 1
        H[ii] = h % 24
    return H

def get_ymd(D):
    Nd = len(D)
    ymd = np.zeros((Nd,3)).astype(int)
    for ii in range(Nd):
        s = D[ii].split('-')
        for nn in range(3):
            ymd[ii,nn] = int(s[nn])
    return ymd
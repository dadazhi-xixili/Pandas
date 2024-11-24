class table:
    def __init__(self, row: tuple):
        self.g = [[row]]
        self.g_sum = [row[1]]

    def add(self, row: tuple):
        for i, v in enumerate(self.g_sum):
            if v + row[1] <= 21:
                self.g[i].append(row)
                self.g_sum[i] += row[1]
                return
        self.g.append([row])
        self.g_sum.append(row[1])

    def add_all(self, data: list[tuple]):
        for row in data:
            self.add(row)

    def to_df(self):
        import pandas as pd

        df_list = []
        for i, (data, v) in enumerate(zip(self.g, self.g_sum), 1):
            df = pd.DataFrame(data).assign(i=i, v=v)
            df_list.append(df)
        return pd.concat(df_list)


if __name__ == '__main__':
    from openpyxl import load_workbook

    sheet = load_workbook('.小题\按值分组.xlsx')['Sheet1']
    data = list(
        zip(
            (x.value for r in sheet['A3:A224'] for x in r),
            (x.value for r in sheet['E3:E224'] for x in r),
        )
    )
    g = table(data[0])
    g.add_all(data[1:])
    df = g.to_df()
    df.to_excel('.小题\按值分组_r.xlsx')

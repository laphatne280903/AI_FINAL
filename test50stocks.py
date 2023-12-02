import random

def get_max_investment():
    while True:
        try:
            max_investment = float(input("Nhập số tiền đầu tư tối đa: "))
            return max_investment
        except ValueError:
            print("Số tiền đầu tư tối đa không hợp lệ. Hãy nhập lại.")

def filter_stocks(stocks, max_investment):
    filtered_stocks = []
    for stock in stocks:
        if stock[2] <= max_investment:
            filtered_stocks.append(stock)
    return filtered_stocks

def fitness(solution, max_investment):
    total_investment = 0
    total_profit = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            stock = filtered_stocks[i]
            total_investment += stock[2]
            total_profit += stock[1]

    if total_investment > max_investment:
        return 0

    return total_profit

def create_initial_population(population_size):
    population = []
    for _ in range(population_size):
        solution = [random.randint(0, 1) for _ in range(len(filtered_stocks))]
        population.append(solution)
    return population

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(solution, mutation_rate):
    for i in range(len(solution)):
        if random.random() < mutation_rate:
            solution[i] = 1 - solution[i]
    return solution

def find_best_solution(population, max_investment):
    best_solution = None
    best_fitness = 0
    for solution in population:
        current_fitness = fitness(solution, max_investment)
        if current_fitness > best_fitness:
            best_solution = solution
            best_fitness = current_fitness
    return best_solution, best_fitness

def genetic_algorithm(max_investment, selected_stocks):
    population_size = 50
    num_generations = 50
    mutation_rate = 0.1

    global filtered_stocks
    filtered_stocks = filter_stocks(selected_stocks, max_investment)
    print("Các cổ phiếu được mua thành công: ", selected_stocks)
    if not filtered_stocks:
        print("Không đủ tiền đầu tư để mua bất kỳ mã cổ phiếu nào.")
        return None

    best_solution = None
    best_fitness = 0

    population = create_initial_population(population_size)
    for generation in range(num_generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = random.choices(population, k=2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population
        current_best_solution, current_best_fitness = find_best_solution(population, max_investment)

        if current_best_fitness > best_fitness:
            best_solution = current_best_solution
            best_fitness = current_best_fitness

        print(f"Generation {generation}: Best Fitness = {best_fitness}")

    return best_solution


stocks = [ ("AAPL", 0.1, 150),
    ("GOOGL", 0.15, 200),
    ("TSLA", 0.2, 250),
    ("AMZN", 0.12, 180),
    ("MSFT", 0.07, 210),
    ("MTA", 0.01, 130),
    ("MOIT", 0.21, 250),
    ("QUIT", 0.05, 125),
    ("ABC", 0.03, 120),
    ("XYZ", 0.08, 180),
    ("DEF", 0.09, 160),
    ("GHI", 0.11, 200),
    ("JKL", 0.06, 190),
    ("MNO", 0.04, 170),
    ("PQR", 0.02, 140),
    ("STU", 0.18, 220),
    ("VWX", 0.14, 240),
    ("YZA", 0.13, 230),
    ("BCD", 0.16, 260),
    ("EFG", 0.17, 270),
    ("HIJ", 0.19, 280),
    ("KLM", 0.22, 300),
    ("NOP", 0.23, 310),
    ("QRS", 0.25, 320),
    ("TUV", 0.24, 330),
    ("WXY", 0.26, 340),
    ("ZAB", 0.27, 350),
    ("CDE", 0.28, 360),
    ("FGH", 0.29, 370),
    ("IJK", 0.30, 380),
    ("LMN", 0.31, 390),
    ("OPQ", 0.32, 400),
    ("RST", 0.33, 410),
    ("UVW", 0.34, 420),
    ("XYZ", 0.35, 430),
    ("123", 0.36, 440),
    ("456", 0.37, 450),
    ("789", 0.38, 460),
    ("000", 0.39, 470),
    ("111", 0.40, 480),
    ("222", 0.41, 490),
    ("333", 0.42, 500),
    ("444", 0.43, 510),
    ("555", 0.44, 520),
    ("666", 0.45, 530),
    ("777", 0.46, 540),
    ("888", 0.47, 550),
    ("999", 0.48, 560),
    ("000", 0.49, 570),
    ("AAA", 0.50, 580)]

selected_stocks = []          

         







from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton


class Ui_MainWindow(object):

    
    def display_result(self, best_solution, max_investment):
     if best_solution:
         msg = QMessageBox()
         msg.setWindowTitle("Best Solution")
         content = "Best solution:\n"
         total_investment = 0
         for i, invest in enumerate(best_solution):
             if invest == 1:
                 stock = filtered_stocks[i]
                 content += f"Invest in {stock[0]} (Expected ROI: {stock[1]})\n"
                 total_investment += stock[2]

         content += f"Total investment: {total_investment}\n"
         content += f"Best fitness: {fitness(best_solution, max_investment)}"
         msg.setText(content)
         msg.exec_()
     else:
        print("Không tìm thấy giải pháp tốt nhất.")

    def setup_selected_list(self, tableWidget):
      tableWidget.setColumnCount(4)  # Số lượng cột là 4
      
      tableWidget.setHorizontalHeaderLabels(["Mã cổ phiếu", "Tỉ lệ tăng giá", "Giá tiền cổ phiếu"," "])
      tableWidget.verticalHeader().setVisible(False)
      tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section {border-bottom: 1px solid #d8d8d8;}")
      tableWidget.setColumnWidth(0, 150) 
      tableWidget.setColumnWidth(1, 150)  
      tableWidget.setColumnWidth(2, 150)  
      tableWidget.setColumnWidth(3, 100)  

    # Bổ sung hàm xử lý sự kiện khi nút "Mua" được nhấn
    def handle_Confirm(self):
    
  
     global stocks
     selected_stocks = []
     for row in range(self.Selected_List.rowCount()):
         stock_code = self.Selected_List.item(row, 0).text()
         stock_profit = float(self.Selected_List.item(row, 1).text())
         stock_price = float(self.Selected_List.item(row, 2).text())
         selected_stocks.append((stock_code, stock_profit, stock_price))

     stocks.extend(selected_stocks)
     money_input_text = self.Money_Input.text()
     try:
            Max_Invest = float(money_input_text)  # Chuyển đổi giá trị thành số dấu phẩy động
            best_solution = genetic_algorithm(Max_Invest, selected_stocks)
            self.display_result(best_solution, Max_Invest)
     except ValueError:
            QtWidgets.QMessageBox.warning(MainWindow, 'Lỗi', 'Hãy nhập giá trị hợp lệ')

        
        
  

    def add_stocks_to_table_widget(self, tableWidget, stocks):
        tableWidget.setColumnCount(4)  # Số lượng cột là 4
        tableWidget.setRowCount(len(stocks))

        # Thiết lập tiêu đề cho từng cột
        tableWidget.setHorizontalHeaderLabels(["Mã cổ phiếu", "Tỉ lệ tăng giá", "Giá tiền cổ phiếu", " "])

        # Thêm dữ liệu vào từng ô tương ứng
        for i, stock in enumerate(stocks):
            for j in range(3):
                item = QtWidgets.QTableWidgetItem(str(stock[j]))
                item.setTextAlignment(Qt.AlignCenter)
                tableWidget.setItem(i, j, item)
            button = QPushButton("Thêm")
            button.clicked.connect(lambda _, row=i: self.handle_button_click(stocks[row]))  # Gắn hàm xử lý sự kiện khi nút được nhấn
            tableWidget.setCellWidget(i, 3, button)

        # Thiết lập độ rộng của các cột 
        tableWidget.setColumnWidth(0, 200)  # Cột 0
        tableWidget.setColumnWidth(1, 200)  # Cột 1
        tableWidget.setColumnWidth(2, 200)  # Cột 2
        tableWidget.setColumnWidth(3, 140)  # Cột 3
    
    def delete_row(self, row):
         if self.Selected_List.rowCount() == 1:
          self.Selected_List.setRowCount(0)
          return
         self.Selected_List.removeRow(row)

    def add_delete_button(self, row):
        delete_button = QtWidgets.QPushButton("Xóa")
        delete_button.clicked.connect(lambda _, r=row: self.delete_row(r))
        self.Selected_List.setCellWidget(row, 3, delete_button)
    
    def check_existing_stock_code(self, stock_code):
        row_count = self.Selected_List.rowCount()
        for row in range(row_count):
         item = self.Selected_List.item(row, 0)
         if item is not None and item.text() == stock_code:
            return True
        return False

    def handle_button_click(self, stock):
     stock_code = stock[0]
     if not self.check_existing_stock_code(stock_code):
         row_count = self.Selected_List.rowCount()
         self.Selected_List.setRowCount(row_count + 1)

         self.Selected_List.setItem(row_count, 0, QtWidgets.QTableWidgetItem(stock[0]))
         self.Selected_List.setItem(row_count, 1, QtWidgets.QTableWidgetItem(str(stock[1])))
         self.Selected_List.setItem(row_count, 2, QtWidgets.QTableWidgetItem(str(stock[2])))

         self.add_delete_button(row_count)

     else:
         print(f"Cổ phiếu {stock_code} đã có trong danh sách.")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1510, 847)
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Select_Stock = QtWidgets.QLabel(self.centralwidget)
        self.Select_Stock.setGeometry(QtCore.QRect(1070, 10, 311, 31))
        self.Select_Stock.setMinimumSize(QtCore.QSize(311, 31))
        self.Select_Stock.setSizeIncrement(QtCore.QSize(3, 3))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Select_Stock.setFont(font)


        self.Select_Stock.setObjectName("Select_Stock")
        self.Select_List_Scroller = QtWidgets.QScrollArea(self.centralwidget)
        self.Select_List_Scroller.setGeometry(QtCore.QRect(810, 40, 681, 441))
        self.Select_List_Scroller.setWidgetResizable(True)
        self.Select_List_Scroller.setObjectName("Select_List_Scroller")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 679, 439))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.Selected_List = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.Selected_List.setGeometry(QtCore.QRect(0, 0, 681, 441))
        self.Selected_List.setObjectName("Selected_List")
        self.Selected_List.setColumnCount(0)
        self.Selected_List.setRowCount(0)

        #SetUp cho list mình chọn
        self.setup_selected_list(self.Selected_List)

        self.Select_List_Scroller.setWidget(self.scrollAreaWidgetContents_2)
     
        
      
        self.Stock_List_Scroller = QtWidgets.QScrollArea(self.centralwidget)
        self.Stock_List_Scroller.setGeometry(QtCore.QRect(10, 40, 781, 441))
        self.Stock_List_Scroller.setWidgetResizable(True)
        self.Stock_List_Scroller.setObjectName("Stock_List_Scroller")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 779, 439))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.Stock_List = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_5)
        self.Stock_List.setGeometry(QtCore.QRect(0, 0, 791, 451))
        self.Stock_List.setObjectName("Stock_List")
        self.Stock_List.setColumnCount(0)
        self.Stock_List.setRowCount(0)
        # them co phieu
        self.add_stocks_to_table_widget(self.Stock_List,stocks)

        self.Stock_List_Scroller.setWidget(self.scrollAreaWidgetContents_5)
        self.Choose_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Choose_Button.setGeometry(QtCore.QRect(1110, 490, 161, 41))
        self.Choose_Button.setObjectName("Choose_Button")

        self.Choose_Button.clicked.connect(self.handle_Confirm)


        
        self.Stock_label = QtWidgets.QLabel(self.centralwidget)
        self.Stock_label.setGeometry(QtCore.QRect(290, 10, 311, 31))
        self.Stock_label.setMinimumSize(QtCore.QSize(311, 31))
        self.Stock_label.setSizeIncrement(QtCore.QSize(3, 3))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Stock_label.setFont(font)
        self.Stock_label.setObjectName("Stock_label")
        self.Money_Label = QtWidgets.QLabel(self.centralwidget)
        self.Money_Label.setGeometry(QtCore.QRect(180, 490, 311, 31))
        self.Money_Label.setMinimumSize(QtCore.QSize(311, 31))
        self.Money_Label.setSizeIncrement(QtCore.QSize(3, 3))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Money_Label.setFont(font)
        self.Money_Label.setObjectName("Money_Label")
        self.Money_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Money_Input.setGeometry(QtCore.QRect(350, 490, 201, 41))
        self.Money_Input.setObjectName("Money_Input")
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1510, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Select_Stock.setText(_translate("MainWindow", "Cổ phiếu bạn đã chọn"))
        self.Choose_Button.setText(_translate("MainWindow", "Mua"))
        self.Stock_label.setText(_translate("MainWindow", "Cổ phiếu trên sàn"))
        self.Money_Label.setText(_translate("MainWindow", "Số tiền hiện có: "))
       


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    


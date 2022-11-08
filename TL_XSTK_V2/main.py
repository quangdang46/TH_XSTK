# Part 1
'''
mean()
fmean()
geometric_mean()
harmonic_mean()
median()
median_low()
median_high()
median_grouped()
mode()
multimode()
quantiles()
pstdev()
pvariance()
stdev()
variance()
covariance()
correlation()
linear_regression()
'''
'''
cách sử dụng,
tham số đầu vào,
ý nghĩa của kết quả trả về,
mã ví dụ.
'''
from statistics import *
from math import *


# 1 mean()
'''
Mô tả:Hàm mean() dùng để tính trung bình cộng của một dãy số truyền vào.Trung bình cộng trong thống kê là một đại lượng mô tả thống kê, được tính ra bằng cách lấy tổng giá trị của toàn bộ các phần tử trong tập chia cho số lượng các phần tử trong tập.
Giá trị trung bình của mẫu đưa ra một ước tính không chệch về giá trị trung bình của tổng thể thực, để khi lấy trung bình trên tất cả các mẫu có thể, sẽ mean(sample)hội tụ về giá trị trung bình thực của toàn bộ tổng thể. Nếu dữ liệu đại diện cho toàn bộ tổng thể thay vì một mẫu, thì mean(data)tương đương với việc tính giá trị trung bình tổng thể thực sự
Cách sử dung:mean(data)
Tham số đầu vào: data là một dãy số
Kết quả trả về: Trung bình cộng của dãy số truyền vào
'''
# Ví dụ:
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data1 = [1, 1,2,3]
print(mean(data))  # 5.0
print(mean(data1))  # 1.75

# 2 fmean()
'''
Mô tả: Hàm fmean() dùng để tính trung bình cộng của một dãy số truyền vào.
Điểm khác biệt giữa fmean() và mean() là fmean() sử dụng kiểu dữ liệu float để tính toán, còn mean() sử dụng kiểu dữ liệu int và fmean() chạy nhanh hơn mean().
Cách sử dung:fmean(data)
Tham số đầu vào: data là một dãy số
Kết quả trả về: Trung bình cộng của dãy số truyền vào dưới dạng dấu phẩy động
'''
# Ví dụ:
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data1 = [1, 1,2,3]
print(fmean(data))  # 5.0
print(fmean(data1))  # 1.75

# 3 geometric_mean()
'''
Mô tả: Hàm geometric_mean() dùng để tính trung bình hình học của một dãy số truyền vào.
Trung bình hình học là một đại lượng thống kê được sử dụng để tính toán trung bình của các giá trị số dương. Trung bình hình học được tính bằng cách lấy tích của các giá trị số dương, sau đó lấy căn bậc hai của tích đó.
Trung bình hình học biểu thị xu hươnhs trong tâm của tập dữ liệu, và nó có thể được sử dụng để tính toán tỷ lệ trung bình của các giá trị số dương.
Trung bình hình học khác với trung bình cộng trong trường hợp các giá trị số âm, vì trung bình hình học không thể được tính toán với các giá trị số âm.
Cách sử dung:geometric_mean(data)
Tham số đầu vào: data là một dãy số
Kết quả trả về: Trung bình hình học của dãy số truyền vào
'''
# Ví dụ:
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data1 = [1, 1,2,3]
print(geometric_mean(data))  # 4.528728688116168
print(geometric_mean(data1))  # 1.5874010519681994

# 4 harmonic_mean()
'''
Mô tả: Hàm harmonic_mean() dùng để tính trung bình hàm của một dãy số truyền vào.
Trung bình điều hoà là một đại lượng thống kê được sử dụng để tính toán trung bình của các giá trị số dương. Trung bình điều hoà được tính bằng cách lấy nghịch đảo của các giá trị số dương, sau đó lấy nghịch đảo của trung bình của các giá trị số dương đó.
Cách sử dung:harmonic_mean(data)
Tham số đầu vào: data là một dãy số
Kết quả trả về: Trung bình hàm của dãy số truyền vào
'''
# Ví dụ:
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data1 = [1, 1,2,3]
print(harmonic_mean(data))  # 3.414171521474055
print(harmonic_mean(data1))  # 1.3333333333333333

# 5 median()
'''
Mô tả: Hàm median() dùng để tính giá trị trung vị của một dãy số truyền vào.
Giá trị trung vị là một số tách giữa nửa lớn hơn và nửa bé hơn của một mẫu, một quần thể, hay một phân bố xác suất. Nó là giá trị giữa trong một phân bố, mà số các số nằm trên hay dưới con số đó là bằng nhau.
Một nữa số lượng các số trong một phân bố là số lượng các số nhỏ hơn giá trị trung vị, và nửa còn lại là số lượng các số lớn hơn giá trị trung vị.
Số trung vị của một danh sách là giá trị nằm giữa nếu số lượng các phần tử là số lẻ, hoặc là trung bình của hai giá trị nằm giữa nếu số lượng các phần tử là số chẵn.
Cách sử dung:median(data)
Tham số đầu vào: data là một dãy số
Kết quả trả về: Giá trị trung vị của dãy số truyền vào
'''
# Ví dụ:
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data1 = [1, 1,2,3]
print(median(data))  # 5
print(median(data1))  # 1.5

# 6 median_low()
'''
Mô tả: Hàm median_low() dùng để tính giá trị trung vị nhỏ nhất của một dãy số truyền vào.
giá trị trung vị nhỏ nhất là giá trị trung vị của một dãy số khi các số trong dãy số được sắp xếp theo thứ tự tăng dần.
Nếu dãy số có số lượng phần tử là số lẻ thì giá trị trung vị nhỏ nhất là giá trị ở vị trí giữa của dãy số.
Nếu dãy số có số lượng phần tử là số chẵn thì giá trị trung vị nhỏ nhất là giá trị ở vị trí giữa của dãy số.

Cách sử dung:median_low(data)
Tham số đầu vào: data là một dãy số
Kết quả trả về: Giá trị trung vị nhỏ nhất của dãy số truyền vào
'''
# Ví dụ:
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data1 = [1, 1,2,3]
print(median_low(data))  # 5
print(median_low(data1))  # 1

# 7 median_high()
'''
Mô tả: Hàm median_high() dùng để tính giá trị trung vị lớn nhất của một dãy số truyền vào.
giá trị trung vị lớn nhất là giá trị trung vị của một dãy số khi các số trong dãy số được sắp xếp theo thứ tự giảm dần.
Nếu dãy số có số lượng phần tử là số lẻ thì giá trị trung vị lớn nhất là giá trị ở vị trí giữa của dãy số.
Nếu dãy số có số lượng phần tử là số chẵn thì giá trị trung vị lớn nhất là giá trị ở vị trí giữa của dãy số.
Cách sử dung:median_high(data)
Tham số đầu vào: data là một dãy số
Kết quả trả về: Giá trị trung vị lớn nhất của dãy số truyền vào
'''
# Ví dụ:
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data1 = [1, 1,2,3]
print(median_high(data))  # 5
print(median_high(data1))  # 2

# 8 median_grouped()
'''
Mô tả: Hàm median_grouped() dùng để tính giá trị trung vị của một dãy số truyền vào.
giá trị trung vị là giá trị trung bình của giá trị trung vị nhỏ nhất và giá trị trung vị lớn nhất.
Cách sử dung:median_grouped(data, interval=1)
Tham số đầu vào: data là một dãy số
interval là khoảng cách giữa các giá trị trong dãy số
Kết quả trả về: Giá trị trung vị của dãy số truyền vào
'''
# Ví dụ:
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data1 = [1, 1,2,3]
print(median_grouped(data))  # 5
print(median_grouped(data1))  # 1.5

# 9 mode()
'''
Mô tả: Hàm mode() dùng để tính giá trị xuất hiện nhiều nhất của một dãy số truyền vào.
Nếu có nhiều giá trị xuất hiện nhiều nhất thì hàm mode() sẽ trả về giá trị nhỏ nhất trong các giá trị đó.
Cách sử dung:mode(data)
Tham số đầu vào: data là một dãy số
Kết quả trả về: Giá trị xuất hiện nhiều nhất của dãy số truyền vào
'''
# Ví dụ:
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data1 = [1, 1,2,3]
print(mode(data))  # 1
print(mode(data1))  # 1

# 10 multimode()
'''
Mô tả: Hàm multimode() dùng để tính giá trị xuất hiện nhiều nhất của một dãy số truyền vào.
Nếu có nhiều giá trị xuất hiện nhiều nhất thì hàm multimode() sẽ trả về tất cả các giá trị đó.
Cách sử dung:multimode(data)
Tham số đầu vào: data là một dãy số
Kết quả trả về: Danh sách các iá trị xuất hiện nhiều nhất của dãy số truyền vào
'''
# Ví dụ:
data = [1, 2,2,3,1,3,4,4,4,5,5,5]
data1 = [1, 1,2,3]
print(multimode(data))  # [1]
print(multimode(data1))  # [1, 2, 3]

# 11 quantiles()
'''
Mô tả: Hàm quantiles() dùng để tính các giá trị phân vị của một dãy số truyền vào.
Các điểm phân vị là các điểm mà dãy số được chia thành các phần bằng nhau.
Cách sử dung:quantiles(data, n=4)
Tham số đầu vào: data là một dãy số
n là số lượng phân vị cần tính
Kết quả trả về: Danh sách các giá trị phân vị của dãy số truyền vào
'''
# Ví dụ:
data = [1, 2,2,3,1,3,4,4,4,5,5,5]
data1 = [1, 1,2,3]
print(quantiles(data))  # [1.0, 2.0, 4.0, 5.0]
print(quantiles(data1))  # [1.0, 1.0, 2.0, 3.0]

# 12 pstdev()
'''
Mô tả: Hàm pstdev() dùng để tính độ lệch chuẩn của một quần thể.
Độ lệch chuẩn là độ lệch trung bình của các giá trị trong dãy số truyền vào so với giá trị trung bình của dãy số đó.
là một đại lượng thống kê dùng để đo mức độ phân tán của một tập dữ liệu đã được lập thành bảng tần số. Có thể tính ra độ lệch chuẩn bằng cách lấy căn bậc hai của phương sai. Khi hai tập dữ liệu có cùng giá trị trung bình cộng, tập nào có độ lệch chuẩn lớn hơn là tập có dữ liệu biến thiên nhiều hơn. Trong trường hợp hai tập dữ liệu có giá trị trung bình cộng không bằng nhau, thì việc so sánh độ lệch chuẩn của chúng không có ý nghĩa. Độ lệch chuẩn còn được sử dụng khi tính sai số chuẩn. Khi lấy độ lệch chuẩn chia cho căn bậc hai của số lượng quan sát trong tập dữ liệu, sẽ có giá trị của sai số chuẩn.
Cách sử dung:pstdev(data)
Tham số đầu vào: data là một dãy số
Kết quả trả về: Độ lệch chuẩn của dãy số truyền vào
'''
# Ví dụ:
data = [1, 2,2,3,1,3,4,4,4,5,5,5]
data1 = [1, 1,2,3]
print(pstdev(data))  # 1.4142135623730951
print(pstdev(data1))  # 0.816496580927726

# 13 pvariance()
'''
Mô tả: Hàm pvariance() dùng để tính phương sai của một quần thể.
phương sai là giá trị kỳ vọng của bình phương của độ lệch của X so với giá trị trung bình của nó. Nói nôm na, phương sai là "trung bình của bình phương khoảng cách của mỗi điểm dữ liệu tới điểm trung bình". Do đó, nó là giá trị trung bình của bình phương độ lệch.
Cách sử dung:pvariance(data)
Tham số đầu vào: data là một dãy số
Kết quả trả về: Phương sai của dãy số truyền vào
'''
# Ví dụ:
data = [1, 2,2,3,1,3,4,4,4,5,5,5]
data1 = [1, 1,2,3]
print(pvariance(data))  # 2.0
print(pvariance(data1))  # 0.6666666666666666

# 14 stdev()
'''
Mô tả: Hàm stdev() dùng để tính độ lệch chuẩn của một mẫu.
Độ lệch chuẩn là độ lệch trung bình của các giá trị trong dãy số truyền vào so với giá trị trung bình của dãy số đó.
là một đại lượng thống kê dùng để đo mức độ phân tán của một tập dữ liệu đã được lập thành bảng tần số. Có thể tính ra độ lệch chuẩn bằng cách lấy căn bậc hai của phương sai. Khi hai tập dữ liệu có cùng giá trị trung bình cộng, tập nào có độ lệch chuẩn lớn hơn là tập có dữ liệu biến thiên nhiều hơn. Trong trường hợp hai tập dữ liệu có giá trị trung bình cộng không bằng nhau, thì việc so sánh độ lệch chuẩn của chúng không có ý nghĩa. Độ lệch chuẩn còn được sử dụng khi tính sai số chuẩn. Khi lấy độ lệch chuẩn chia cho căn bậc hai của số lượng quan sát trong tập dữ liệu, sẽ có giá trị của sai số chuẩn.
Cách sử dung:stdev(data)
Tham số đầu vào: data là một dãy số
Kết quả trả về: Độ lệch chuẩn của dãy số truyền vào
'''
# Ví dụ:
data = [1, 2,2,3,1,3,4,4,4,5,5,5]
data1 = [1, 1,2,3]
print(stdev(data))  # 1.2909944487358056
print(stdev(data1))  # 0.7453559924999299

# 15 variance()
'''
Mô tả: Hàm variance() dùng để tính phương sai của một mẫu.
phương sai là giá trị kỳ vọng của bình phương của độ lệch của X so với giá trị trung bình của nó. Nói nôm na, phương sai là "trung bình của bình phương khoảng cách của mỗi điểm dữ liệu tới điểm trung bình". Do đó, nó là giá trị trung bình của bình phương độ lệch.
Cách sử dung:variance(data)
Tham số đầu vào: data là một dãy số
Kết quả trả về: Phương sai của dãy số truyền vào
'''
# Ví dụ:
data = [1, 2,2,3,1,3,4,4,4,5,5,5]
data1 = [1, 1,2,3]
print(variance(data))  # 2.0
print(variance(data1))  # 0.6666666666666666

# 16 covariance()
'''
Mô tả: Hàm covariance() dùng để hiệp phương sai là độ đo sự biến thiên cùng nhau của hai biến ngẫu nhiên
Hiệp phương sai được tính bằng cách phân tích các biến động về lãi suất (độ lệch chuẩn so với lợi nhuận kì vọng) hoặc bằng cách nhân mối tương quan giữa hai biến với độ lệch chuẩn của từng biến.
Cách sử dung:covariance(data1, data2)
Tham số đầu vào: data1, data2 là hai dãy số
Kết quả trả về: Hiệp phương sai của hai dãy số truyền vào
'''
# Ví dụ:
data1 = [1, 2,2,3,1,3,4,4,4,5,5,5]
data2 = [1, 1,2,3,1,3,4,4,4,5,5,5]
print(covariance(data1, data2))  # 2.0

# 17 correlation()
'''
Mô tả: Hàm correlation() dùng để tính độ tương quan giữa hai dãy số
Hệ số tương quan là một chỉ số đo lường của một số loại tương quan, nghĩa là mối liên hệ thống kê giữa hai biến số.[1] Các biến có thể là hai cột của một bộ dữ liệu quan sát đã cho, thường được gọi là mẫu hoặc hai phần của một biến ngẫu nhiên đa biến số có phân phối đã biết trước.
Có một số loại hệ số tương quan, mỗi loại lại có định nghĩa riêng, phạm vi sử dụng và đặc tính riêng. Tất cả đều giả định các giá trị nằm trong phạm vi chạy từ −1 đến +1, trong đó ± 1 biểu thị hai biến số có mối tương quan tuyệt đối có thể và 0 chỉ hai biến số không có liên hệ gì với nhau.[2] Là công cụ phân tích, các hệ số tương quan thể hiện một số vấn đề nhất định, bao gồm khuynh hướng của một số loại yếu tố nhiễu bởi ngoại lai và khả năng được sử dụng tương đối để suy ra mối quan hệ nhân quả giữa các biến số.[3]
Cách sử dung:correlation(data1, data2)
Tham số đầu vào: data1, data2 là hai dãy số
Kết quả trả về: Độ tương quan của hai dãy số truyền vào
'''
# Ví dụ:
data1 = [1, 2,2,3,1,3,4,4,4,5,5,5]
data2 = [1, 1,2,3,1,3,4,4,4,5,5,5]
print(correlation(data1, data2))  # 1.0

# 18 linear_regression()
'''
Mô tả: Hàm linear_regression() dùng để tính hệ số hồi quy tuyến tính
Hồi quy tuyến tính là một trong những phương pháp phân tích dữ liệu phổ biến nhất. Nó được sử dụng để dự đoán mối quan hệ giữa một biến phụ thuộc và một hoặc nhiều biến độc lập. Hồi quy tuyến tính được sử dụng để dự đoán mối quan hệ giữa một biến phụ thuộc và một hoặc nhiều biến độc lập. Hồi quy tuyến tính được sử dụng để dự đoán mối quan hệ giữa một biến phụ thuộc và một hoặc nhiều biến độc lập. Hồi quy tuyến tính được sử dụng để dự đoán mối quan hệ giữa một biến phụ thuộc và một hoặc nhiều biến độc lập.
Cách sử dung:linear_regression(data1, data2)
Tham số đầu vào: data1, data2 là hai dãy số
Kết quả trả về: Hệ số hồi quy tuyến tính của hai dãy số truyền vào
'''
# Ví dụ:
data1 = [1, 2,2,3,1,3,4,4,4,5,5,5]
data2 = [1, 1,2,3,1,3,4,4,4,5,5,5]
print(linear_regression(data1, data2))  # 1.0






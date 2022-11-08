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
from fractions import Fraction as F

# 1 mean()
'''
mean()được sử dụng để tính giá trị trung bình của một danh sách các số nhất định.
Nó trả về giá trị trung bình của tập dữ liệu được truyền dưới dạng tham số.
Trung bình là tổng dữ liệu chia cho số lượng phần tử của dữ liệu.
Nó là thước đo vị trí trung tâm của dữ liệu trong một tập hợp các giá trị khác nhau trong phạm vi
Cú pháp : mean ([data-set])
Tham số:  [data-set] : Danh sách của một tập hợp số.
Trả về: Trung bình cộng của dữ liệu truyền vào.
Ngoại lệ : Xảy ra khi bất kỳ tham số truyền khác ngoài giá trị số được truyền dưới dạng tham số. 
'''

# 2 fmean()
'''
fmean () chuyển đổi tất cả dữ liệu thành kiểu dữ liệu float và sau đó tính giá trị trung bình số học hoặc giá trị trung bình của dữ liệu được cung cấp.
Đầu ra của hàm này luôn là một float.
Sự khác biệt duy nhất trong tính toán có nghĩa là sử dụng mean () và fmean () là trong khi sử dụng fmean (), dữ liệu được chuyển đổi thành float trong khi trong trường hợp mean (), dữ liệu không được chuyển đổi thành float. Hơn nữa, hàm fmean () chạy nhanh hơn hàm mean ().
Cú pháp: fmean ([data-set}])
Tham số: [data-set]: Danh sách hoặc bộ số của một tập hợp số.
Trả về: giá trị trung bình số học dấu phẩy động của dữ liệu được cung cấp.
Ngoại lệ: StatisticsError. Được nâng lên khi tập dữ liệu trống
'''
fmean()

# 3 geometric_mean()
'''
Trong số học, trung bình hình học được định nghĩa là giá trị trung bình trong đó các số của một dãy được nhân với nhau và sau đó tính căn thứ n của nó, trong đó n là số giá trị trong dãy đó. Nó có thể được hiểu là căn thứ n của tích n giá trị.
Bằng cách tính gốc tích các giá trị của chúng, giá trị trung bình hình học biểu thị xu hướng trọng tâm của một tập hợp các số
Chuyển đổi dữ liệu thành float và tính giá trị trung bình hình học.
Giá trị trung bình hình học cho biết xu hướng trung tâm hoặc giá trị điển hình của dữ liệu bằng cách sử dụng tích của các giá trị (trái ngược với giá trị trung bình số học sử dụng tổng của chúng).
Tăng StatisticsError nếu tập dữ liệu đầu vào trống, nếu nó chứa số 0 hoặc nếu nó chứa giá trị âm.
'''
geometric_mean()

# 4 harmonic_mean()
'''
Trung bình hài hòa (còn được gọi là Trung bình trái ngược) là một trong một số loại trung bình và đặc biệt là một trong những phương tiện Pitago. Thường được sử dụng trong các tình huống khi tỷ giá trung bình được mong muốn.
Trung bình điều hòa cũng là nghịch đảo của trung bình cộng của các nghịch đảo của một tập hợp quan sát nhất định.
Trả về giá trị trung bình hài của dữ liệu , một chuỗi hoặc có thể lặp lại của các số có giá trị thực. Nếu trọng số bị bỏ qua hoặc Không có , thì trọng số bằng nhau được giả định.
Cú pháp: harmonic_mean ([data-set])
Tham số:  
[data-set] : là một danh sách hoặc bộ hoặc bộ lặp của các số thực có giá trị.
Kiểu trả về: Trả về harmonic_mean của tập dữ liệu đã cho.
Lỗi và Ngoại lệ:
StatisticsError khi một tập dữ liệu trống được chuyển qua hoặc nếu tập dữ liệu bao gồm các giá trị âm. 
TypeError cho tập dữ liệu của các giá trị kiểu không phải số. 
StatisticsErrorđược nâng lên nếu dữ liệu trống, bất kỳ phần tử nào nhỏ hơn 0 hoặc nếu tổng trọng số không dương.

Giá trị trung bình điều hòa là nghịch đảo của số học mean()với nghịch đảo của dữ liệu. Ví dụ, trung bình điều hòa của ba giá trị a , b và c sẽ tương đương với . Nếu một trong các giá trị là 0, kết quả sẽ là 0.3/(1/a + 1/b + 1/c)
Trung bình hài hòa là một loại giá trị trung bình, là thước đo vị trí trung tâm của dữ liệu. Nó thường thích hợp khi lấy tỷ lệ hoặc tỷ lệ trung bình, ví dụ như tốc độ.
# input: data is a list of numbers
# output: the harmonic mean of the data
# example: harmonic_mean([1,2,3,4,5]) = 2.18978102189781
'''
print(harmonic_mean([1,2,3,4]))

# 5 median()
'''
Trung vị là giá trị phân tách nửa cao hơn của mẫu dữ liệu hoặc phân phối xác suất với nửa dưới. Đối với một tập dữ liệu, nó có thể được coi là giá trị trung bình. Trung vị là thước đo xu hướng trọng tâm của các thuộc tính của tập dữ liệu trong thống kê và lý thuyết xác suất. Median có một lợi thế rất lớn so với Mean, đó là giá trị trung vị không bị lệch quá nhiều bởi các giá trị cực kỳ lớn hay nhỏ. Giá trị trung bình được chứa trong tập dữ liệu các giá trị được cung cấp hoặc nó không thay đổi quá nhiều so với dữ liệu được cung cấp.
Đối với tập hợp các phần tử lẻ , giá trị trung vị là giá trị giữa. 
Đối với tập hợp các phần tử chẵn , giá trị trung vị là giá trị trung bình của hai phần tử ở giữa.
Cú pháp: median (data)
Tham số:
data: là một danh sách hoặc bộ hoặc bộ lặp của các số thực có giá trị.
Kiểu trả về: Trả về giá trị trung vị của tập dữ liệu đã cho.
Lỗi và Ngoại lệ:
StatisticsError khi một tập dữ liệu trống được chuyển qua hoặc nếu tập dữ liệu bao gồm các giá trị âm.

Cú pháp: median ( [data-set] )
Tham số:  
[data-set] : Danh sách hoặc bộ hoặc một có thể lặp với tập hợp các giá trị số
Trả về: Trả về giá trị trung bình (giá trị giữa) của có thể lặp có chứa dữ liệu
Ngoại lệ: Thống kê Lỗi được nâng lên khi có thể lặp được truyền là trống hoặc khi danh sách rỗng. 

'''

print(median([1,2,3,4,5]))


# 6 median_low()
'''
 Trung vị thấp luôn là một thành viên của tập dữ liệu. Khi số điểm dữ liệu là số lẻ, giá trị giữa được trả về. Khi nó là số chẵn, giá trị nhỏ hơn trong hai giá trị ở giữa được trả về. Hãy xem median_low () hoạt động như thế nào.
Cú pháp: median_low ( [data-set] ) 
Tham số: [data-set] : Đưa vào danh sách, bộ dữ liệu hoặc tập hợp dữ liệu số có thể lặp lại. 
Kiểu trả về: Trả về giá trị trung bình thấp của dữ liệu số. Mức trung bình thấp là một thành viên của tập dữ liệu thực tế. 
Ngoại lệ: StatisticsError xuất hiện khi tập dữ liệu trống.

'''
def median_low(data):
  n = len(data)
  if n < 1:
      raise StatisticsError('no median for empty data')
  data = sorted(data)
  midpoint = n // 2
  if n % 2:
      return data[midpoint]
  else:
      return data[midpoint - 1]

# 7 median_high()
'''
Trung vị cao luôn là một thành viên của tập dữ liệu. Khi số điểm dữ liệu là số lẻ, giá trị giữa được trả về. Khi nó là số chẵn, giá trị lớn hơn trong hai giá trị giữa được trả về. Hãy xem hàm median_high () hoạt động như thế nào.

Cú pháp: median_high ( [data - set] ) 

Tham số: [data-set] : Đưa vào danh sách hoặc một tập hợp dữ liệu số có thể lặp lại. 

Kiểu trả về: Trả về giá trị trung bình cao của dữ liệu số (luôn nằm trong tập dữ liệu thực tế). 

Ngoại lệ: StatisticsError xuất hiện khi tập dữ liệu trống.
'''
def median_high(data):
  n = len(data)
  if n < 1:
      raise StatisticsError('no median for empty data')
  data = sorted(data)
  midpoint = n // 2
  return data[midpoint]

# 8 median_grouped()
'''
Hàm median_grouped () trong mô-đun Thống kê, giúp tính toán giá trị trung bình từ một tập dữ liệu liên tục.
Dữ liệu được giả định là được nhóm lại thành các khoảng có khoảng chiều rộng. Mỗi điểm dữ liệu trong mảng là điểm giữa của khoảng chứa giá trị thực. Giá trị trung bình được tính bằng cách nội suy trong khoảng trung vị (khoảng chứa giá trị trung vị), giả sử rằng các giá trị thực trong khoảng đó được phân phối đồng nhất:
Cú pháp: median_grouped ([data-set], khoảng thời gian)
Tham số:  
[data-set]: Danh sách hoặc bộ giá trị hoặc có thể lặp lại với một tập các giá trị số. 
khoảng thời gian (1 theo mặc định) : Xác định độ rộng của dữ liệu được nhóm và thay đổi. Nó cũng sẽ thay đổi nội suy của giá trị trung vị được tính toán.
Kiểu trả về: Trả về giá trị trung bình của dữ liệu liên tục được nhóm lại, được tính bằng phân vị thứ 50 .
Ngoại lệ: StatisticsError xuất hiện khi có thể lặp được truyền vào trống hoặc khi danh sách rỗng. 
'''
median_grouped()
# 9 mode()
'''
Chế độ của một tập hợp các giá trị dữ liệu là giá trị xuất hiện thường xuyên nhất . Đây là giá trị mà dữ liệu có nhiều khả năng được lấy mẫu nhất. Chế độ của phân phối xác suất liên tục thường được coi là bất kỳ giá trị x nào mà tại đó hàm mật độ xác suất của nó có giá trị cực đại cục bộ, vì vậy bất kỳ đỉnh nào cũng là một chế độ.
Python rất mạnh mẽ khi nói đến thống kê và làm việc với một tập hợp các giá trị lớn. Mô-đun thống kê có một số lượng rất lớn các chức năng để làm việc với các tập dữ liệu rất lớn. Hàm mode () là một trong những phương thức như vậy. Hàm này trả về số đo mạnh mẽ của một điểm dữ liệu trung tâm trong một phạm vi tập dữ liệu nhất định.
Cú pháp: mode (data)
Tham số:
data: Danh sách hoặc bộ giá trị hoặc có thể lặp lại với một tập các giá trị số.
Kiểu trả về: Trả về một danh sách chứa các giá trị mạnh mẽ nhất của tập dữ liệu.
Ngoại lệ: StatisticsError xuất hiện khi có thể lặp được truyền vào trống hoặc khi danh sách rỗng.

'''
def Counter(data):
  cnt = {}
  for x in data:
    cnt[x] = cnt.get(x, 0) + 1
  return cnt

def mode(data):
  n = len(data)
  if n == 0:
      raise StatisticsError('no mode for empty data')
  elif n == 1:
      return data[0]
  counts = Counter(data)
  maxcount = max(counts.values())
  return min(num for num, count in counts.items() if count == maxcount)

# 10 multimode()
'''
Trả lại danh sách các giá trị xuất hiện thường xuyên nhất theo thứ tự lần đầu tiên chúng gặp trong dữ liệu . Sẽ trả về nhiều hơn một kết quả nếu có nhiều chế độ hoặc danh sách trống nếu dữ liệu trống:
Phương multimode()thức này được sử dụng để lấy danh sách các giá trị dữ liệu phổ biến nhất (chế độ). Nếu có các giá trị có cùng tần suất, thì các giá trị được trả về theo thứ tự xuất hiện của chúng.
Phương thức trả về một danh sách trống nếu không có dữ liệu nào được cung cấp cho hàm.
'''
def multimode(data):
  n = len(data)
  if n == 0:
      raise StatisticsError('no mode for empty data')
  elif n == 1:
      return data[0]
  counts = Counter(data)
  maxcount = max(counts.values())
  return sorted(num for num, count in counts.items() if count == maxcount)

# 11 quantiles()
'''
# usage: Return a list of n-1 quantiles, or n equally-spaced cuts in the data. If n is not provided, it defaults to 4, returning quartiles. If data is empty, StatisticsError will be raised.
The quantiles are the values separating the lower and upper halves of a data sample. The lower quartile is the median of the lower half of the data; the upper quartile is the median of the upper half. The interquartile range is the difference between the upper and lower quartiles.
# Lỗi

Chia dữ liệu thành n khoảng liên tục với xác suất bằng nhau. Trả về danh sách n - 1 điểm cắt tách các khoảng.

Đặt n thành 4 cho phần tư (mặc định). Đặt n thành 10 cho các deciles. Đặt n thành 100 cho các phân vị, cung cấp 99 điểm cắt để phân tách dữ liệu thành 100 nhóm có kích thước bằng nhau. Tăng Thống kê Lỗi nếu n không nhỏ nhất 1.

Dữ liệu có thể là bất kỳ có thể lặp lại nào có chứa dữ liệu mẫu. Để có kết quả có ý nghĩa, số lượng điểm dữ liệu trong dữ liệu phải lớn hơn n. Tăng Thống kê Lỗi nếu không có ít nhất hai điểm dữ liệu.

Các điểm cắt được nội suy tuyến tính từ hai điểm dữ liệu gần nhất. Ví dụ: nếu một điểm cắt giảm 1/3 khoảng cách giữa hai giá trị mẫu, 100 và 112, điểm cắt sẽ đánh giá là 104.

Phương pháp tính toán lượng tử có thể khác nhau tùy thuộc vào việc dữ liệu bao gồm hay loại trừ các giá trị thấp nhất và cao nhất có thể khỏi tập hợp.

Phương pháp mặc định là "độc quyền" và được sử dụng cho dữ liệu được lấy mẫu từ một tập hợp có thể có nhiều giá trị cực đoan hơn được tìm thấy trong các mẫu. Phần dân số giảm xuống dưới thứ i của m điểm dữ liệu được sắp xếp được tính là i / (m + 1). Đưa ra chín giá trị mẫu, phương pháp sắp xếp chúng và gán các phân vị sau: 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%.

Đặt phương pháp thành "bao gồm" được sử dụng để mô tả dữ liệu dân số hoặc cho các mẫu được biết là bao gồm các giá trị cực đoan nhất từ ​​tổng thể. Giá trị nhỏ nhất trong dữ liệu được coi là phân vị thứ 0 và giá trị lớn nhất được coi là phân vị thứ 100. Phần dân số giảm xuống dưới thứ i của m điểm dữ liệu được sắp xếp được tính là (i - 1) / (m - 1). Với 11 giá trị mẫu, phương pháp sắp xếp chúng và gán các phân vị sau: 0%, 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%.
'''
quantiles()

# 12 pstdev()
'''
cung cấp một hàm được gọi là stdev () , có thể được sử dụng để tính toán độ lệch chuẩn. Hàm stdev () chỉ tính toán độ lệch chuẩn từ một mẫu dữ liệu, thay vì toàn bộ tập hợp. 

Độ lệch chuẩn là thước đo độ chênh lệch trong Thống kê. Nó được sử dụng để định lượng thước đo mức độ lan truyền, sự biến đổi của một tập hợp các giá trị dữ liệu. Nó rất giống với phương sai, cho phép đo độ lệch trong khi phương sai cung cấp giá trị bình phương. 
Phép đo Độ lệch chuẩn thấp cho thấy dữ liệu ít bị dàn trải hơn, trong khi giá trị Độ lệch chuẩn cao cho thấy dữ liệu trong một tập hợp được trải ra ngoài các giá trị trung bình trung bình của chúng. Một thuộc tính hữu ích của độ lệch chuẩn là, không giống như phương sai, nó được biểu thị bằng các đơn vị giống như dữ liệu. 
ú pháp: stdev ([data-set], xbar)
Tham số:  
[data]: Có thể lặp lại với các số thực có giá trị. 
xbar (Tùy chọn) : Lấy giá trị trung bình thực tế của tập dữ liệu.
Returnype: Trả về độ lệch chuẩn thực tế của các giá trị được truyền dưới dạng tham số.
Ngoại lệ:  
StatisticsError được đưa ra đối với tập dữ liệu ít hơn 2 giá trị được truyền dưới dạng tham số. 
Giá trị không thể / không chính xác khi giá trị được cung cấp dưới dạng xbar không khớp với giá trị trung bình thực của tập dữ liệu. 
'''
pstdev()

# 13 pvariance()
'''
pvariance () giúp tính toán phương sai của toàn bộ, thay vì của một mẫu. Sự khác biệt duy nhất giữa phương sai () và pvariance () là trong khi sử dụng phương sai (), chỉ giá trị trung bình của mẫu được xem xét, trong khi trong pvariance (), giá trị trung bình của toàn bộ tập hợp được xem xét.
Phương sai tổng thể cũng tương tự như phương sai mẫu, nó cho biết cách các điểm dữ liệu trong một tập hợp cụ thể được trải ra như thế nào. Nó là giá trị trung bình của khoảng cách từ điểm dữ liệu đến giá trị trung bình của tập dữ liệu, được bình phương. Phương sai tổng thể là một tham số của tổng thể và không phụ thuộc vào phương pháp nghiên cứu hoặc thực hành lấy mẫu. 
 

Cú pháp: pvariance ([data], mu)
Tham số: 
[data]: Có thể lặp với các số thực có giá trị. 
mu (tùy chọn): Lấy giá trị trung bình thực tế của tập dữ liệu / tập hợp dữ liệu.
Kiểu trả về: Trả về phương sai tổng thể thực tế của các giá trị được truyền dưới dạng tham số.
Ngoại lệ:  
StatisticsError được đưa ra đối với tập dữ liệu ít hơn 2 giá trị được truyền dưới dạng tham số. 
Giá trị không thể có khi giá trị được cung cấp dưới dạng mu không khớp với giá trị trung bình thực của tập dữ liệu. 
'''
pvariance()
# 14 stdev()
'''
: Trả về độ lệch chuẩn mẫu (thước đo mức độ lan truyền hoặc phân tán của một bộ giá trị) của dữ liệu, chuỗi các số có giá trị thực.
Độ lệch chuẩn mẫu là căn bậc hai của phương sai mẫu.
# usage: Return the sample standard deviation (a measure of the spread or dispersion of a set of values) of data, the sequence of real-valued numbers.
The sample standard deviation is the square root of the sample variance.
# input: data is a list of numbers
# output: the sample standard deviation of the data
# example: stdev([1,2,3,4,5]) = 1.5811388300841898
'''
stdev()

# 15 variance()
'''
phương sai () là một trong những hàm như vậy. Hàm này giúp tính toán phương sai từ một mẫu dữ liệu (mẫu là một tập hợp con của dữ liệu được phổ biến). 
Hàm variance () chỉ nên được sử dụng khi phương sai của một mẫu cần được tính toán. Có một hàm khác được gọi là pvariance (), được sử dụng để tính toán phương sai của toàn bộ tập hợp.
Trong thống kê thuần túy, phương sai là độ lệch bình phương của một biến so với giá trị trung bình của nó. Về cơ bản, nó đo lường sự lan truyền của dữ liệu ngẫu nhiên trong một tập hợp từ giá trị trung bình hoặc giá trị trung bình của nó. Giá trị thấp cho phương sai chỉ ra rằng dữ liệu được nhóm lại với nhau và không được phân tán rộng rãi, trong khi giá trị cao sẽ chỉ ra rằng dữ liệu trong tập hợp đã cho được phân tán nhiều hơn ngoài giá trị trung bình. 
Phương sai là một công cụ quan trọng trong khoa học, nơi phân tích thống kê dữ liệu là phổ biến. Nó là bình phương độ lệch chuẩn của tập dữ liệu đã cho và còn được gọi là thời điểm trung tâm thứ hai của phân phối.
ú pháp: variance ([data], xbar)
Tham số: 
[data]: Có thể lặp với các số thực có giá trị. 
xbar (Tùy chọn): Lấy giá trị trung bình thực tế của tập dữ liệu.
Returnype: Trả về phương sai thực tế của các giá trị được truyền dưới dạng tham số.
Ngoại lệ:  
StatisticsError được đưa ra đối với tập dữ liệu ít hơn 2 giá trị được truyền dưới dạng tham số. 
Ném các giá trị không thể thực hiện được khi giá trị được cung cấp dưới dạng xbar không khớp với giá trị trung bình thực tế của tập dữ liệu. 
'''
variance()

# 16 covariance()
'''
Trả về hiệp phương sai mẫu của hai đầu vào x và y . Hiệp phương sai là thước đo sự thay đổi chung của hai đầu vào.
Cả hai đầu vào phải có cùng độ dài (không ít hơn hai),
Đó là mối quan hệ giữa một cặp biến ngẫu nhiên trong đó sự thay đổi của một biến gây ra sự thay đổi trong biến khác.
Nó có thể nhận bất kỳ giá trị nào trong khoảng từ -infinity đến + infinity, trong đó giá trị âm đại diện cho mối quan hệ âm trong khi giá trị dương đại diện cho mối quan hệ dương.
Nó được sử dụng cho mối quan hệ tuyến tính giữa các biến.
Nó đưa ra hướng quan hệ giữa các biến.
'''
covariance()

# 17 correlation()
'''
Trả về hệ số tương quan của Pearson cho hai đầu vào. Hệ số tương quan r của Pearson nhận các giá trị từ -1 đến +1. Nó đo độ mạnh và hướng của mối quan hệ tuyến tính, trong đó +1 có nghĩa là mối quan hệ tuyến tính rất mạnh, tích cực, -1 rất mạnh, mối quan hệ tuyến tính tiêu cực và 0 không có mối quan hệ tuyến tính nào.
Cả hai đầu vào phải có cùng độ dài (không ít hơn hai) và không cần phải không đổi, nếu không StatisticsErrorsẽ được nâng lên.
Nó cho biết liệu các cặp biến số có liên quan với nhau hay không và mức độ mạnh mẽ như thế nào.
Tương quan nhận các giá trị từ -1 đến +1, trong đó các giá trị gần +1 thể hiện mối tương quan dương mạnh mẽ và giá trị gần -1 thể hiện mối tương quan âm mạnh.
Trong biến này có quan hệ gián tiếp với nhau.
Nó cung cấp hướng và độ mạnh của mối quan hệ giữa các biến.
'''
correlation()
# 18 linear_regression()
'''
Hồi quy tuyến tính cơ bản
Hồi quy tuyến tính đơn giản là một cách tiếp cận để dự đoán phản hồi bằng cách sử dụng một tính năng duy nhất .
Giả thiết rằng hai biến có quan hệ tuyến tính với nhau. Do đó, chúng tôi cố gắng tìm một hàm tuyến tính dự đoán giá trị phản hồi (y) chính xác nhất có thể như một hàm của đối tượng địa lý hoặc biến độc lập (x).
'''
# def linear_regression(data1, data2):
#   n = len(data1)
#   if n != len(data2):
#       raise StatisticsError('data sequences must have the same length')
#   if n < 2:
#       raise StatisticsError('variance requires at least two data points')
#   xbar = mean(data1)
#   ybar = mean(data2)
#   ssx = sum((x - xbar) ** 2 for x in data1)
#   ssxy = sum((x - xbar) * (y - ybar) for x, y in zip(data1, data2))
#   try:
#       slope = ssxy / ssx
#   except ZeroDivisionError:
#       slope = float('inf')
#   intercept = ybar - slope * xbar
#   return slope, intercept

linear_regression()




# Part 2
'''
Histogram equalization algorithm for image processing. 
- Survey about the problem, histogram approach, formula, algorithm... 
- Write an illustrative program.
'''
# 1. Survey about the problem, histogram approach, formula, algorithm...
'''
Histogram equalization is a method in image processing of contrast adjustment using the image's histogram.
The histogram equalization algorithm is used to improve the contrast in an image, in order to stretch out the intensity range. This is useful in images with low contrast, as they often appear in scanned photographs.
The algorithm works by transforming the values in the input image so that the output image has a uniform histogram. The algorithm works by mapping the input gray levels to output gray levels based on the cumulative distribution function of the input image.
The cumulative distribution function (CDF) is the probability that a variable takes a value less than or equal to x. For a given gray level i, the CDF is the fraction of pixels in the image with a value less than or equal to i.
The histogram equalization algorithm is as follows:
1. Calculate the histogram of the image.
2. Calculate the cumulative distribution function (CDF).
3. For each pixel in the image, replace the value with the value of the CDF at that pixel's intensity level.
4. Normalize the image to the range [0, 255].
'''

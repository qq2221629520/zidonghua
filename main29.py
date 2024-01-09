import os
from docx import Document

def extract_data_from_docx(docx_path):
    doc = Document(docx_path)
    data_dict = {}

    for table in doc.tables:
        for row in table.rows:
            row_cells = list(row.cells)  # 将元组转换为列表
            for cell in row_cells:
                if "额定速度" in cell.text:
                    index = row_cells.index(cell)
                    if index + 1 < len(row_cells):
                        next_cell = row_cells[index + 2]
                        data_dict[os.path.basename(docx_path)] = next_cell.text.strip()
                        return data_dict

    return data_dict

def process_all_docx_files(folder_path):
    data_dict = {}

    for filename in os.listdir(folder_path):
        if filename.endswith(".docx"):
            file_path = os.path.join(folder_path, filename)
            data_dict.update(extract_data_from_docx(file_path))

    return data_dict

# 指定文件夹路径
folder_path = r"D:\个人资料\电梯\电梯限速器动作速度校检报告 山东润华物业管理有限公司潍坊分公司 28个\电梯年度自行检验报告"

# 处理所有docx文件
result_dict = process_all_docx_files(folder_path)

# 打印结果
for filename, value in result_dict.items():
    print(f"{filename}: {value}")

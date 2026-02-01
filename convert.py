import json

# 初始化变量，与你要求一致
results = ""
split_tab = "  "  # 缩进符，保持你的定义

if __name__ == "__main__":
    # 1. 读取JSON文件（外层是list的标准JSON）
    # 替换为你的JSON文件实际路径，指定utf-8编码避免中文乱码
    json_file_path = "C:/Users/拖拖/Desktop/part_2_1(修改后).json"
    # 替换为你的TXT文件输出路径
    txt_file_path = "C:/Users/拖拖/Desktop/part_2_1(修改后).txt"

    try:
        # 读取JSON文件并解析为Python列表
        with open(json_file_path, "r", encoding="utf-8") as f:
            json_data_list = json.load(f)

        # 2. 遍历每条数据，按指定格式拼接字符串
        for line in json_data_list:
            if line['input_final_status'] == 'CONFIRMED_VALID':
                continue
            # 注意：你的JSON中字段是"_index"，不是"index"，已修正（避免KeyError）
            new_str = "\"_index\":\"" + str(line["_index"]) + "\"\n"\
                + "\"input_SQL\":\"" + line['input_SQL'] + "\"\n"\
                + "\"input_OLD_SQL\":\"" + line['input_OLD_SQL'] + "\"\n"\
                + split_tab + "\"input_question\":\"" + line['input_question'] + "\"\n"\
                + split_tab + "\"input_evidence\":\"" + line['input_evidence'] + "\"\n" \
                + split_tab + "\"input_audit_analysis\":\"" + line['input_audit_analysis'] + "\"\n" \
                + split_tab + "\"input_audit_reason\":\"" + line['input_audit_reason'] + "\"\n" \
                + "如果两个sql中有一个是正确的，给出正确的是哪一个sql，并给出另一个错误的理由；如果两个sql都是错误的，给出正确的sql，并分别给出两个sql错误的理由。\n\n"
            results += new_str

        # 3. 将拼接后的结果写入TXT文件
        with open(txt_file_path, "w", encoding="utf-8") as f:
            f.write(results)

        print(f"处理完成！结果已保存到：{txt_file_path}")
        print(f"共处理 {len(json_data_list)} 条数据")

    except FileNotFoundError:
        print(f"错误：未找到JSON文件，请检查路径是否正确：{json_file_path}")
    except KeyError as e:
        print(f"错误：数据中缺少指定字段：{e}")
    except Exception as e:
        print(f"未知错误：{e}")
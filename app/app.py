from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/train', methods=['POST'])
def upload_csv():
    # 检查请求中是否包含文件/upload_csv
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    # 检查文件名是否为空
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # 读取 CSV 文件
    try:
        df = pd.read_csv(file)
        # 在这里可以对 DataFrame 进行进一步处理，如数据预处理、特征工程等
        # 这里只是简单地将 DataFrame 转换为 JSON 格式并返回
        return df.to_json()
    except Exception as e:
        return jsonify({'error': str(e)})



if __name__ == '__main__':
    app.run(debug=True)

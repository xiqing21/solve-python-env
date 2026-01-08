import random
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import cpu_count

def simulate_person():
    """模拟一个人连续抛20次硬币，判断是否都是正面"""
    for _ in range(20):
        if random.random() < 0.5:
            return False
    return True

def simulate_batch(batch_size):
    """模拟一批人"""
    success_count = 0
    for _ in range(batch_size):
        if simulate_person():
            success_count += 1
    return success_count

def main():
    total_people = 300_000_000  # 3亿人
    batch_size = 1_000_000  # 每批处理100万人
    num_batches = total_people // batch_size

    print(f"开始模拟 {total_people:,} 人连续抛20次硬币...")
    print(f"使用 {cpu_count()} 个CPU核心并行计算")
    print(f"理论概率: {1/(2**20):.10f} ≈ {1/(2**20)*100:.6f}%")
    print(f"理论期望成功人数: {total_people/(2**20):.2f} 人")
    print("-" * 60)

    total_success = 0

    with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        futures = []
        for i in range(num_batches):
            future = executor.submit(simulate_batch, batch_size)
            futures.append((i, future))

        for i, future in futures:
            success_count = future.result()
            total_success += success_count
            progress = (i + 1) / num_batches * 100
            print(f"进度: {progress:.1f}% - 第 {i+1}/{num_batches} 批完成，当前成功人数: {success_count}")

    print("-" * 60)
    print(f"\n最终结果：")
    print(f"模拟总人数: {total_people:,} 人")
    print(f"成功人数: {total_success:,} 人 ({total_success/total_people*100:.6f}%)")
    print(f"理论期望: {total_people/(2**20):.2f} 人")
    print(f"偏差: {(total_success - total_people/(2**20))/total_people/(2**20)*100:.2f}%")

if __name__ == "__main__":
    main()

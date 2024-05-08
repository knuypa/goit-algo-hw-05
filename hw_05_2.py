def binary_search_with_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    while left <= right:
        mid = (left + right) // 2
        iterations += 1
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return (iterations, arr[mid])  # Точне співпадіння

    # Якщо ми вийшли з циклу і не знайшли точне співпадіння, то `left` буде вказувати на найменший елемент, 
    # який більший за target. Перевіримо, щоб `left` не вийшов за межі масиву.
    upper_bound = arr[left] if left < len(arr) else None
    return (iterations, upper_bound)

# Тестування функції
arr = [1.1, 1.5, 2.8, 3.6, 4.7, 5.9]
target = 3.5
print(binary_search_with_upper_bound(arr, target))  # Приклад виклику функції
defmodule Solution do
  def generate(k) do
    1..k
    |> Enum.map(&generate_row/1)
    |> Enum.each(&print_row/1)
  end

  defp generate_row(n) do
    0..(n-1)
    |> Enum.map(fn r -> binomial_coefficient(n-1, r) end)
  end

  defp binomial_coefficient(n, r) do
    factorial(n) |> div(factorial(r) * factorial(n - r))
  end

  defp factorial(0), do: 1
  defp factorial(n), do: n * factorial(n - 1)

  defp print_row(row) do
    row
    |> Enum.join(" ")
    |> IO.puts()
  end

  def main do
    k = IO.read(:line) |> String.trim() |> String.to_integer()

    if k >= 2 and k <= 10 do
      generate(k)
    end
  end
end

k = IO.read(:line) |> String.trim() |> String.to_integer()

if k >= 2 and k <= 10 do
  Solution.generate(k)
end

# PascalsTriangle.main()

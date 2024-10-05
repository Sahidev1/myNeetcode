

defmodule Solution do
  @spec is_anagram(s :: String.t, t :: String.t) :: boolean
    def is_anagram(s, t) do
      s_charl = String.to_charlist(s)
      t_charl = String.to_charlist(t)
      fill_map(%{}, s_charl)|>pop_char(t_charl)
    end

    def fill_map(map, []) do map end
    def fill_map(map, [charcode|str]) do
      count = Map.get(map, charcode, 0)
      Map.put(map, charcode, count + 1)|>fill_map(str)
    end


    def pop_char(map, []) when map_size(map) == 0 do true end
    def pop_char(map, _) when map_size(map) == 0 do false end
    def pop_char(_, []) do false end
    def pop_char(map, [charcode|str]) do
      count = Map.get(map, charcode, 0)
      if count > 1 do
        pop_char(Map.put(map, charcode, count - 1), str)
      else
        pop_char(Map.delete(map, charcode), str)
      end
    end

  end

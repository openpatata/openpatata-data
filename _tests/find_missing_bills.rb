
=begin
finds bills missing in the sequence btn the first and last bill we've
got for each bill type/year
=end

def find_missing_bills
  g = {:type   => nil,
       :period => nil,
       :count  => nil,
       :year   => nil}

  Dir[File.join("bills", "*.yaml")].sort.each do |filename|
    # using a hash saves us the trouble of assigning each to outer scope
    # individually at the bottom
    l = {}
    _,    # '23' is constant -- discard it
    l[:type], l[:period],
    l[:count], l[:year] = filename.split(/\.|-/)

    # skip earlier years -- we're missing too many bills
    next if l[:year].to_i < 2014

    # reset counter if the type or period's changed
    g[:count] = 0 if g[:type] != l[:type] or
                     g[:period] != l[:period]
    diff = l[:count].to_i - g[:count].to_i - 1
    diff.times do |number|
      missing = (g[:count].to_i + number + 1).to_s.rjust(3, '0')
      puts "23.#{l[:type]}.#{l[:period]}.#{missing}-#{l[:year]}"
    end if diff > 0

    g = l
  end
end

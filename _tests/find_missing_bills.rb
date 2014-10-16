
=begin
finds bills missing in the sequence btn the first and last bill we've
got for each bill type/year
=end

def find_missing_bills
  g = {:type   => nil,
       :period => nil,
       :count  => nil,
       :year   => nil}

  Dir[File.join("bills", "*.yaml")].each do |filename|
    # using a hash saves us the trouble of assigning each to outer scope
    # individually below
    l = {}
    _, l[:type],    # '23' is constant -- discard it
       l[:period],
       l[:count],
       l[:year] = filename.split(/\.|-/)

    # skip earlier years -- we're missing too many bills
    next if l[:year].to_i < 2014

    if (g[:type] == l[:type]) and (g[:period] == l[:period]) and g[:count]
      diff = l[:count].to_i - g[:count].to_i - 1
      diff.times do |number|
        missing = (g[:count].to_i + number + 1).to_s.rjust(3, '0')
        puts "Missing: " +
             "23.#{l[:type]}.#{l[:period]}.#{missing}-#{l[:year]}"
      end if diff > 0
    end

    g = l
  end
end

find_missing_bills

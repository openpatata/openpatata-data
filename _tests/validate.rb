
require 'kwalify'
require 'yaml'

def validate_documents_of_kind(kind)
  validator = Kwalify::Validator.new(
                YAML.load_file(File.join('_tests', 'schemas',
                                         "#{kind.chop}.yaml")))

  Dir[File.join(kind, '*.yaml')].each do |filename|
    errors = validator.validate(YAML.load_file(filename))
    if errors && !errors.empty?
      for error in errors
        puts filename, "[#{error.path}] #{error.message}"
      end
    end
  end
end

validate_documents_of_kind('bills')
validate_documents_of_kind('committee_reports')
validate_documents_of_kind('mps')
validate_documents_of_kind('plenary_sittings')

class Post < ActiveRecord::Base
  self.validates :name, :presence => true
  self.validates :title, :presence => true, :length => {:minimum => 5 }
  
  self.has_many :comments, :dependent => :destroy
  self.has_many :tags

  accepts_nested_attributes_for :tags, :allow_destroy => :true,
    :reject_if => proc { |attrs| attrs.all? { |k, v| v.blank? } }
end

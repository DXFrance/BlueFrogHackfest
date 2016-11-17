using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Microsoft.Hadoop.Avro;
using System.IO;

namespace AvroSample
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                string sampleFilePath = @"..\..\..\..\..\EventHub\SampleData\05";

                var serializer = AvroSerializer.Create<Microsoft.ServiceBus.Messaging.EventData>();
                string content = "";

                using (var file = File.OpenRead(sampleFilePath))
                {
                    var result = serializer.Deserialize(file);
                    using (var bodyStreamReader = new StreamReader(result.GetBodyStream()))
                    {
                        content = bodyStreamReader.ReadToEnd();
                    }
                }

                Console.WriteLine($"content='{content}'");

                Console.WriteLine("OK");
            }
            catch(Exception ex)
            {
                Console.WriteLine($"{ex}");
            }
            finally
            {
                Console.WriteLine("ENTER");
                Console.ReadLine();
            }
        }
    }
}
